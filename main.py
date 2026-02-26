from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib
import json

# --- IMPROVED APP METADATA ---
app = FastAPI(
    title="Blockchain Digital Asset Engine",
    description="""
    ## 🛡️ Regulated Asset Infrastructure
    This system facilitates **Atomic Settlement** and **Immutable Auditing**.
    
    ### Core Components:
    * **Settlement Engine:** Handles peer-to-peer asset transfers.
    * **Audit Ledger:** Provides a transparent, hashed history of all trades.
    """,
    version="1.0.0",
)

# Mock Data
ledger = []
balances = {"SYSTEM_TREASURY": 10000.0, "USER_1": 0.0}

class Transaction(BaseModel):
    sender: str
    receiver: str
    amount: float

class User(BaseModel):
    username: str
    initial_balance: float = 0.0

# --- ORGANIZED ENDPOINTS ---

@app.post("/register", tags=["Onboarding & Compliance"])
def register_user(user: User):
    """
    Onboards a new user to the blockchain Ledger.
    - Sets initial liquidity.
    - Marks user as 'KYC Verified' (Mock).
    """
    if user.username in balances:
        raise HTTPException(status_code=400, detail="User already registered")
    
    balances[user.username] = user.initial_balance
    return {"message": f"User {user.username} registered and KYC verified."}

@app.post("/settle-trade", tags=["Settlement Engine"])
def settle_trade(tx: Transaction):
    # Check if the sender actually exists in our system
    if tx.sender not in balances:
        raise HTTPException(status_code=404, detail=f"Sender '{tx.sender}' not found in registry")

    # Check for funds
    if balances[tx.sender] < tx.amount:
        raise HTTPException(status_code=400, detail="Insufficient Liquidity")

    # Process the trade
    balances[tx.sender] -= tx.amount
    balances[tx.receiver] = balances.get(tx.receiver, 0) + tx.amount

    tx_hash = hashlib.sha256(json.dumps(tx.dict(), sort_keys=True).encode()).hexdigest()
    ledger.append({"data": tx.dict(), "tx_hash": tx_hash})
    return {"status": "Settled", "tx_hash": tx_hash}

@app.get("/ledger", tags=["Audit & Transparency"])
def get_ledger():
    """Returns the complete immutable history of the platform."""
    return ledger