"""
Initialize BioQL Billing Database with Schema and Test Data
"""
import modal
import hashlib
import uuid

billing_volume = modal.Volume.from_name("bioql-billing", create_if_missing=True)
image = modal.Image.debian_slim(python_version="3.11")

app = modal.App(name="init-billing-db", image=image)

@app.function(volumes={"/billing": billing_volume})
def initialize_database():
    """Initialize billing database with schema and test user."""
    import sqlite3

    DB_PATH = "/billing/bioql_billing.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("🔧 Creating database schema...")

    # Create pricing_tiers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pricing_tiers (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            quota_simulator INTEGER DEFAULT 0,
            quota_gpu INTEGER DEFAULT 0,
            quota_quantum INTEGER DEFAULT 0,
            rate_limit_per_minute INTEGER DEFAULT 10,
            price_per_month REAL DEFAULT 0.0
        )
    """)

    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            name TEXT,
            password_hash TEXT NOT NULL,
            current_plan TEXT DEFAULT 'free',
            tier_id TEXT DEFAULT 'tier_free',
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (tier_id) REFERENCES pricing_tiers(id)
        )
    """)

    # Create api_keys table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS api_keys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            key_hash TEXT UNIQUE NOT NULL,
            name TEXT,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Create billing_transactions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS billing_transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            transaction_type TEXT NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Create inference_logs table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inference_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            api_key_id INTEGER NOT NULL,
            prompt TEXT,
            code_generated TEXT,
            time_seconds REAL,
            base_cost REAL,
            user_cost REAL,
            profit REAL,
            success INTEGER,
            error_message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (api_key_id) REFERENCES api_keys(id)
        )
    """)

    print("✅ Schema created successfully\n")

    # Insert default pricing tiers
    print("💰 Creating pricing tiers...")

    tiers = [
        ("tier_free", "Free", 100, 10, 5, 10, 0.0),
        ("tier_starter", "Starter", 1000, 100, 50, 60, 29.0),
        ("tier_pro", "Professional", 10000, 1000, 500, 300, 99.0),
        ("tier_enterprise", "Enterprise", 100000, 10000, 5000, 1000, 499.0),
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO pricing_tiers
        (id, name, quota_simulator, quota_gpu, quota_quantum, rate_limit_per_minute, price_per_month)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, tiers)

    print("✅ Pricing tiers created\n")

    # Create test user
    print("👤 Creating test user...")

    email = "test@bioql.com"
    password = "test123"
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute("""
        INSERT OR IGNORE INTO users (email, name, password_hash, tier_id)
        VALUES (?, ?, ?, ?)
    """, (email, "Test User", password_hash, "tier_pro"))

    # Get user ID
    cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
    user_result = cursor.fetchone()
    user_id = user_result[0] if user_result else None

    if user_id:
        print(f"✅ User created: {email} (ID: {user_id})\n")

        # Create API key
        print("🔑 Creating API key...")
        api_key = f"bioql_test_{uuid.uuid4().hex[:24]}"
        key_hash = hashlib.sha256(api_key.encode()).hexdigest()

        cursor.execute("""
            INSERT INTO api_keys (user_id, key_hash, name, is_active)
            VALUES (?, ?, ?, ?)
        """, (user_id, key_hash, "Test API Key", 1))

        api_key_id = cursor.lastrowid

        print(f"✅ API Key created (ID: {api_key_id})\n")

        # Add initial balance ($100)
        print("💵 Adding initial balance...")
        cursor.execute("""
            INSERT INTO billing_transactions (user_id, amount, transaction_type, description)
            VALUES (?, ?, ?, ?)
        """, (user_id, 100.0, "credit", "Initial balance"))

        print("✅ Balance added: $100.00\n")

        conn.commit()
        billing_volume.commit()
        conn.close()

        print("="*70)
        print("🎉 DATABASE INITIALIZED SUCCESSFULLY!")
        print("="*70)
        print()
        print(f"📧 Email: {email}")
        print(f"🔒 Password: {password}")
        print(f"🔑 API Key: {api_key}")
        print(f"💰 Balance: $100.00")
        print(f"📊 Tier: Professional")
        print()
        print("="*70)
        print()

        return {
            "success": True,
            "api_key": api_key,
            "user_id": user_id,
            "email": email,
            "balance": 100.0
        }
    else:
        conn.close()
        return {"success": False, "error": "Failed to create user"}

@app.local_entrypoint()
def main():
    result = initialize_database.remote()

    if result.get("success"):
        print("🧪 Test the API with this command:\n")
        print(f"""python3 -c "import requests; r = requests.post('https://spectrix--bioql-agent-templates-template-agent.modal.run', json={{'api_key': '{result['api_key']}', 'request': 'dock metformin to AMPK'}}); print(r.json().get('code', r.json()))" """)
        print()
        print("Or use @bioql in VSCode with this API key in settings:")
        print(f"   {result['api_key']}")
    else:
        print(f"❌ Error: {result.get('error')}")
