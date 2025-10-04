"""
Billing Integration for Modal Inference Server
===============================================

Integrates with BioQL billing database for:
- Authentication
- Quota validation
- Usage logging
- Cost tracking
"""

import sqlite3
import hashlib
import uuid
from datetime import datetime
from typing import Optional, Dict, Any, Tuple


# Database will be uploaded as Modal secret/volume
DATABASE_PATH = "/billing/bioql_billing.db"


def authenticate_api_key(api_key: str) -> Optional[Dict[str, Any]]:
    """
    Authenticate user by API key and load billing info.

    Returns user info with quota and balance, or None if invalid.
    """
    if not api_key:
        return {"error": "API key required"}

    try:
        api_key_hash = hashlib.sha256(api_key.encode()).hexdigest()

        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Get user with tier and balance info
        cursor.execute("""
            SELECT
                u.id, u.email, u.name, u.current_plan, u.is_active,
                u.tier_id, ak.id as api_key_id,
                t.name as tier_name,
                t.quota_simulator, t.quota_gpu, t.quota_quantum,
                t.rate_limit_per_minute,
                COALESCE(b.balance, 0.0) as balance
            FROM users u
            JOIN api_keys ak ON u.id = ak.user_id
            LEFT JOIN pricing_tiers t ON u.tier_id = t.id
            LEFT JOIN (
                SELECT user_id, SUM(amount) as balance
                FROM billing_transactions
                GROUP BY user_id
            ) b ON u.id = b.user_id
            WHERE ak.key_hash = ? AND ak.is_active = 1 AND u.is_active = 1
        """, (api_key_hash,))

        result = cursor.fetchone()
        conn.close()

        if not result:
            return {"error": "Invalid or inactive API key"}

        return {
            "user_id": result["id"],
            "email": result["email"],
            "name": result["name"] or "Unknown",
            "plan": result["current_plan"],
            "api_key_id": result["api_key_id"],
            "tier_id": result["tier_id"] or "tier_free",
            "tier_name": result["tier_name"] or "free",
            "quota_gpu": result["quota_gpu"] or 10,
            "rate_limit": result["rate_limit_per_minute"] or 10,
            "balance": float(result["balance"])
        }

    except Exception as e:
        return {"error": f"Authentication failed: {str(e)}"}


def check_sufficient_balance(user_id: str, estimated_cost: float = 0.01) -> Dict[str, Any]:
    """
    Check if user has sufficient balance for the operation.

    Returns: dict with {sufficient: bool, balance: float, message: str}
    """
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        # Get current balance
        cursor.execute("""
            SELECT COALESCE(SUM(amount), 0.0) as balance
            FROM billing_transactions
            WHERE user_id = ?
        """, (user_id,))

        result = cursor.fetchone()
        conn.close()

        balance = result[0] if result else 0.0

        if balance < estimated_cost:
            return {
                "sufficient": False,
                "balance": balance,
                "message": f"Insufficient balance: ${balance:.6f} < ${estimated_cost:.6f}"
            }

        return {
            "sufficient": True,
            "balance": balance,
            "message": f"Balance OK: ${balance:.6f}"
        }

    except Exception as e:
        return {
            "sufficient": False,
            "balance": 0.0,
            "message": f"Balance check failed: {str(e)}"
        }


def log_inference_usage(
    user_id: str,
    api_key_id: str,
    prompt: str,
    code_generated: str,
    time_seconds: float,
    base_cost: float,
    user_cost: float,
    profit: float,
    success: bool = True,
    error_message: str = None
) -> bool:
    """
    Log code generation usage to billing database.

    Returns: True if logged successfully
    """
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        usage_id = str(uuid.uuid4())
        transaction_id = str(uuid.uuid4())
        now = datetime.utcnow().isoformat()

        # Log inference usage
        cursor.execute("""
            INSERT INTO inference_usage (
                id, user_id, api_key_id, prompt, code_generated,
                execution_time, base_cost, user_cost, profit,
                success, error_message, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            usage_id, user_id, api_key_id, prompt[:500], code_generated[:1000],
            time_seconds, str(base_cost), str(user_cost), str(profit),
            success, error_message, now
        ))

        # Create billing transaction (debit user account)
        cursor.execute("""
            INSERT INTO billing_transactions (
                id, user_id, transaction_type, amount, description,
                metadata, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            transaction_id, user_id, "inference_charge", str(-user_cost),
            f"Code generation: {prompt[:50]}...",
            f'{{"usage_id": "{usage_id}", "time_seconds": {time_seconds}}}',
            now
        ))

        conn.commit()
        conn.close()

        return True

    except Exception as e:
        print(f"❌ Failed to log usage: {e}")
        return False


def get_monthly_usage(user_id: str) -> Dict[str, Any]:
    """
    Get current month usage stats for user.

    Returns usage summary with costs and request counts.
    """
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Get current month start
        now = datetime.utcnow()
        month_start = datetime(now.year, now.month, 1).isoformat()

        cursor.execute("""
            SELECT
                COUNT(*) as requests,
                SUM(execution_time) as total_time,
                SUM(CAST(user_cost as REAL)) as total_cost,
                SUM(CAST(profit as REAL)) as total_profit
            FROM inference_usage
            WHERE user_id = ? AND created_at >= ? AND success = 1
        """, (user_id, month_start))

        result = cursor.fetchone()
        conn.close()

        if result:
            return {
                "requests_this_month": result["requests"] or 0,
                "total_time_seconds": result["total_time"] or 0.0,
                "total_cost_usd": result["total_cost"] or 0.0,
                "total_profit_usd": result["total_profit"] or 0.0
            }

        return {
            "requests_this_month": 0,
            "total_time_seconds": 0.0,
            "total_cost_usd": 0.0,
            "total_profit_usd": 0.0
        }

    except Exception as e:
        print(f"❌ Failed to get usage stats: {e}")
        return {
            "requests_this_month": 0,
            "total_time_seconds": 0.0,
            "total_cost_usd": 0.0,
            "total_profit_usd": 0.0,
            "error": str(e)
        }
