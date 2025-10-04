"""
Test authentication function directly
"""
import modal
import hashlib

billing_volume = modal.Volume.from_name("bioql-billing", create_if_missing=True)
image = modal.Image.debian_slim(python_version="3.11")

app = modal.App(name="test-auth", image=image)

@app.function(volumes={"/billing": billing_volume})
def test_auth():
    """Test authentication directly."""
    import sys
    sys.path.insert(0, "/billing")

    # Import the function
    from billing_integration import authenticate_api_key

    api_key = "bioql_test_710344a04088413d8778d6f3"

    print(f"🔑 Testing authentication for: {api_key}\n")

    result = authenticate_api_key(api_key)

    print(f"📊 Result:")
    print(result)

    return result

@app.local_entrypoint()
def main():
    result = test_auth.remote()
    print(f"\n{'='*70}")
    if "error" in result:
        print(f"❌ AUTH FAILED: {result['error']}")
    else:
        print(f"✅ AUTH SUCCESS!")
        print(f"   User ID: {result['user_id']}")
        print(f"   Email: {result['email']}")
        print(f"   Balance: ${result['balance']:.2f}")
    print(f"{'='*70}")
