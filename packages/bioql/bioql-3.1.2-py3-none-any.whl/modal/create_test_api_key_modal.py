"""
Create test API key via Modal
"""
import modal
import hashlib
import uuid

billing_volume = modal.Volume.from_name("bioql-billing", create_if_missing=True)
image = modal.Image.debian_slim(python_version="3.11")

app = modal.App(name="create-test-api-key", image=image)

@app.function(volumes={"/billing": billing_volume})
def create_api_key():
    """Create a test API key with balance."""
    import sqlite3

    DB_PATH = "/billing/bioql_billing.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Test user data
    email = "test@bioql.com"
    password = "test123"
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    # Check if user exists
    cursor.execute("SELECT id, email FROM users WHERE email = ?", (email,))
    existing = cursor.fetchone()

    if existing:
        user_id = existing[0]
        print(f"✅ User already exists: {existing[1]} (ID: {user_id})")
    else:
        # Create user
        cursor.execute(
            "INSERT INTO users (email, password_hash, balance) VALUES (?, ?, ?)",
            (email, password_hash, 100.0)
        )
        user_id = cursor.lastrowid
        print(f"✅ Created user: {email} (ID: {user_id})")

    # Create API key
    api_key = f"bioql_test_{uuid.uuid4().hex[:24]}"

    cursor.execute(
        "INSERT INTO api_keys (user_id, key_hash, name, is_active) VALUES (?, ?, ?, ?)",
        (user_id, hashlib.sha256(api_key.encode()).hexdigest(), "Test Key", 1)
    )
    api_key_id = cursor.lastrowid

    # Add balance
    cursor.execute(
        "UPDATE users SET balance = 100.0 WHERE id = ?",
        (user_id,)
    )

    billing_volume.commit()
    conn.commit()
    conn.close()

    print(f"✅ Created API key: {api_key}")
    print(f"✅ API Key ID: {api_key_id}")
    print(f"✅ Balance: $100.00")
    print()
    print(f"🔑 USE THIS API KEY:")
    print(f"   {api_key}")
    print()

    return {
        "api_key": api_key,
        "user_id": user_id,
        "balance": 100.0
    }

@app.local_entrypoint()
def main():
    result = create_api_key.remote()
    print(f"\n{'='*70}")
    print(f"🔑 YOUR TEST API KEY:")
    print(f"{'='*70}")
    print(f"\n   {result['api_key']}\n")
    print(f"{'='*70}")
    print(f"\n📝 Now test with:")
    print(f'   @bioql dock metformin to AMPK')
    print(f"\n   (Make sure to set this API key in VSCode settings)")
    print(f"{'='*70}\n")
