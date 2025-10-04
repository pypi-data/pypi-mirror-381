"""
Verify API key exists in database
"""
import modal
import hashlib

billing_volume = modal.Volume.from_name("bioql-billing", create_if_missing=True)
image = modal.Image.debian_slim(python_version="3.11")

app = modal.App(name="verify-db", image=image)

@app.function(volumes={"/billing": billing_volume})
def verify():
    """Verify database contents."""
    import sqlite3

    DB_PATH = "/billing/bioql_billing.db"
    api_key = "bioql_test_710344a04088413d8778d6f3"
    key_hash = hashlib.sha256(api_key.encode()).hexdigest()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    print("🔍 Checking database contents...\n")

    # Check tables exist
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print(f"📋 Tables: {[t['name'] for t in tables]}\n")

    # Check users
    cursor.execute("SELECT id, email, is_active FROM users")
    users = cursor.fetchall()
    print(f"👥 Users ({len(users)}):")
    for user in users:
        print(f"   - ID: {user['id']}, Email: {user['email']}, Active: {user['is_active']}")
    print()

    # Check API keys
    cursor.execute("SELECT id, user_id, key_hash, is_active FROM api_keys")
    keys = cursor.fetchall()
    print(f"🔑 API Keys ({len(keys)}):")
    for key in keys:
        print(f"   - ID: {key['id']}, User: {key['user_id']}, Active: {key['is_active']}")
        print(f"     Hash: {key['key_hash'][:20]}...")
    print()

    # Check if our specific key exists
    print(f"🔎 Looking for API key: {api_key}")
    print(f"   Hash: {key_hash[:20]}...\n")

    cursor.execute("""
        SELECT ak.*, u.email, u.is_active as user_active
        FROM api_keys ak
        JOIN users u ON ak.user_id = u.id
        WHERE ak.key_hash = ?
    """, (key_hash,))

    result = cursor.fetchone()

    if result:
        print("✅ API Key FOUND!")
        print(f"   - API Key ID: {result['id']}")
        print(f"   - User ID: {result['user_id']}")
        print(f"   - Email: {result['email']}")
        print(f"   - API Key Active: {result['is_active']}")
        print(f"   - User Active: {result['user_active']}")
    else:
        print("❌ API Key NOT FOUND in database!")

    # Check balance
    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0.0) as balance
        FROM billing_transactions
        WHERE user_id = 1
    """)
    balance_result = cursor.fetchone()
    print(f"\n💰 Balance for user ID 1: ${balance_result['balance']:.2f}")

    conn.close()

@app.local_entrypoint()
def main():
    verify.remote()
