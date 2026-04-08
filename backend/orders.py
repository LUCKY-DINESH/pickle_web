from fastapi import APIRouter, Depends
from .auth import get_current_user
from .database import db
from bson import ObjectId
router = APIRouter()

@router.post("/add_to_cart/{pickle_id}")
def add_to_cart(pickle_id: str, user=Depends(get_current_user)):
    db.carts.update_one(
        {"user": user['username']},
        {"$push": {"items": pickle_id}},
        upsert=True
    )
    return {"message": "Added to cart"}

@router.get("/cart/")
def view_cart(user=Depends(get_current_user)):
    cart = db.carts.find_one({"user": user['username']})
    if not cart: return []
    
    items = cart.get("items", [])
    if not items: return []

    # Calculate item frequencies for quantities
    item_counts = {}
    for i in items:
        item_counts[i] = item_counts.get(i, 0) + 1
        
    pickles = list(db.pickles.find({"_id": {"$in": [ObjectId(i) for i in item_counts.keys()]}}))
    
    result = []
    # Convert ObjectId to string for JSON serialization and append quantity
    for p in pickles:
        p["_id"] = str(p["_id"])
        p["quantity"] = item_counts[p["_id"]]
        result.append(p)
        
    return result

@router.delete("/remove_from_cart/{pickle_id}")
def remove_from_cart(pickle_id: str, user=Depends(get_current_user)):
    db.carts.update_one(
        {"user": user['username']},
        {"$pull": {"items": pickle_id}}
    )
    return {"message": "Removed from cart"}
