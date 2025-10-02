"""
Shopping Agent Demo

Demonstrates how to use the ZeroProof SDK to secure an AI shopping agent.
This example shows the complete flow: challenge creation, proof verification,
and conditional action execution.
"""

import os
import sys
from typing import Dict, Any

# Add parent directory to path for local testing
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from zeroproof import ZeroProof, ZeroProofError
import hashlib


def generate_mock_proof(challenge_id: str, nonce: str, agent_id: str) -> str:
    """
    Generate a mock proof for demo purposes.
    
    In production, this would be replaced with actual cryptographic proof
    generation using zero-knowledge proof libraries.
    """
    # For MVP, create a simple hash-based proof
    proof_data = f"{challenge_id}:{nonce}:{agent_id}"
    return hashlib.sha256(proof_data.encode()).hexdigest()


def add_to_cart(item_id: str, price: float) -> Dict[str, Any]:
    """Simulate adding an item to shopping cart."""
    print(f"\n💳 Adding to cart: {item_id} (${price:.2f})")
    return {
        "cart_id": "CART-123",
        "item_id": item_id,
        "price": price,
        "status": "added"
    }


def process_checkout(amount: float) -> Dict[str, Any]:
    """Simulate processing a checkout."""
    print(f"\n💰 Processing checkout: ${amount:.2f}")
    return {
        "order_id": "ORD-456",
        "amount": amount,
        "status": "completed"
    }


def main():
    """Run the shopping agent demo."""
    
    # Get API key from environment or use demo key
    api_key = os.getenv("ZEROPROOF_API_KEY", "zkp_demo_key")
    
    if api_key == "zkp_demo_key":
        print("⚠️  Using demo API key. Set ZEROPROOF_API_KEY environment variable for production.")
        print("    Example: export ZEROPROOF_API_KEY='zkp_your_actual_key'\n")
    
    # Initialize the ZeroProof client
    try:
        client = ZeroProof(api_key=api_key)
        print("✅ ZeroProof client initialized\n")
    except ValueError as e:
        print(f"❌ Error: {e}")
        return 1
    
    # ========================================
    # SCENARIO 1: Add Item to Cart
    # ========================================
    print("="*60)
    print("SCENARIO 1: Agent Adding Item to Cart")
    print("="*60)
    
    try:
        # Step 1: Agent requests to add item to cart
        print("\n📦 Agent wants to add laptop to cart...")
        
        # Step 2: Create verification challenge
        challenge = client.create_challenge(
            agent_id="shopping-assistant-v1",
            action="add_to_cart",
            context={
                "item_id": "laptop-macbook-pro-16",
                "price": 2499.99,
                "quantity": 1
            }
        )
        
        print(f"✅ Challenge created:")
        print(f"   ID: {challenge.challenge_id}")
        print(f"   Nonce: {challenge.nonce[:16]}...")
        print(f"   Expires in: {challenge.expires_in} seconds")
        
        # Step 3: Agent generates proof (simulated for demo)
        proof = generate_mock_proof(
            challenge.challenge_id,
            challenge.nonce,
            "shopping-assistant-v1"
        )
        print(f"\n🔐 Agent generated proof: {proof[:16]}...")
        
        # Step 4: Verify the proof
        print("\n🔍 Verifying proof...")
        result = client.verify_proof(
            challenge_id=challenge.challenge_id,
            proof=proof,
            agent_signature="demo_signature_here"
        )
        
        # Step 5: Execute action if verified
        if result.verified:
            print(f"\n✅ VERIFICATION SUCCESSFUL!")
            print(f"   Agent: {result.agent_id}")
            print(f"   Action: {result.action}")
            print(f"   Confidence: {result.confidence * 100:.1f}%")
            print(f"   Session: {result.session_id}")
            
            # Now safe to execute the actual e-commerce action
            cart_result = add_to_cart("laptop-macbook-pro-16", 2499.99)
            print(f"   ✅ Cart updated: {cart_result['cart_id']}")
        else:
            print("\n❌ VERIFICATION FAILED - Action blocked!")
            
    except ZeroProofError as e:
        print(f"\n❌ ZeroProof Error: {e.message}")
        if e.status_code:
            print(f"   Status Code: {e.status_code}")
        if e.response:
            print(f"   Response: {e.response}")
    
    # ========================================
    # SCENARIO 2: Process Checkout
    # ========================================
    print("\n" + "="*60)
    print("SCENARIO 2: Agent Processing Checkout")
    print("="*60)
    
    try:
        # Create challenge for checkout
        print("\n💳 Agent wants to process checkout...")
        
        challenge = client.create_challenge(
            agent_id="checkout-agent-v2",
            action="process_payment",
            context={
                "cart_id": "CART-123",
                "amount": 2499.99,
                "currency": "USD",
                "payment_method": "credit_card"
            }
        )
        
        print(f"✅ Challenge created: {challenge.challenge_id}")
        
        # Generate and verify proof
        proof = generate_mock_proof(
            challenge.challenge_id,
            challenge.nonce,
            "checkout-agent-v2"
        )
        
        print(f"🔐 Agent generated proof")
        print("🔍 Verifying proof...")
        
        result = client.verify_proof(
            challenge_id=challenge.challenge_id,
            proof=proof,
            agent_signature="demo_signature_here"
        )
        
        if result.verified and result.confidence > 0.95:
            print(f"\n✅ VERIFICATION SUCCESSFUL! (Confidence: {result.confidence * 100:.1f}%)")
            
            # Process the payment
            order = process_checkout(2499.99)
            print(f"   ✅ Order completed: {order['order_id']}")
        else:
            print(f"\n⚠️  Confidence too low ({result.confidence * 100:.1f}%) - Payment blocked")
            
    except ZeroProofError as e:
        print(f"\n❌ ZeroProof Error: {e.message}")
    
    # ========================================
    # SCENARIO 3: Check Verification Status
    # ========================================
    print("\n" + "="*60)
    print("SCENARIO 3: Checking Verification Status")
    print("="*60)
    
    try:
        print(f"\n🔍 Checking status of session: {challenge.challenge_id}")
        
        status = client.get_status(challenge.challenge_id)
        
        print(f"\n📊 Session Status:")
        print(f"   Status: {status['status']}")
        print(f"   Agent: {status['agent_id']}")
        print(f"   Action: {status['action']}")
        print(f"   Created: {status['created_at']}")
        print(f"   Verified: {status['verified_at']}")
        print(f"   Confidence: {status['confidence'] * 100:.1f}%")
        
    except ZeroProofError as e:
        print(f"\n❌ Error checking status: {e.message}")
    
    # Clean up
    client.close()
    
    print("\n" + "="*60)
    print("Demo completed successfully! ✅")
    print("="*60)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
