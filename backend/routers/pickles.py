from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from bson import ObjectId
import cloudinary.uploader

from ..database import db
from ..auth import require_admin

router = APIRouter()

# ---------------- ADD PICKLE (ADMIN ONLY) ---------------- #

@router.post("/add/", dependencies=[Depends(require_admin)])
async def add_pickle(
    name: str = Form(...),
    category: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    file: UploadFile = File(...)
):
    try:
        upload_result = cloudinary.uploader.upload(file.file)
        image_url = upload_result["secure_url"]

        db.pickles.insert_one({
            "name": name,
            "category": category,
            "description": description,
            "price": price,
            "image_url": image_url
        })

        return {"message": "Pickle added successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------------- UPDATE PICKLE (ADMIN ONLY) ---------------- #

@router.put("/update/{pickle_id}", dependencies=[Depends(require_admin)])
async def update_pickle(
    pickle_id: str,
    name: str = Form(...),
    category: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    file: UploadFile = File(None)
):
    update_data = {
        "name": name,
        "category": category,
        "description": description,
        "price": price
    }

    if file and file.filename:
        upload_result = cloudinary.uploader.upload(file.file)
        update_data["image_url"] = upload_result["secure_url"]

    result = db.pickles.update_one(
        {"_id": ObjectId(pickle_id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Pickle not found")

    return {"message": "Pickle updated successfully"}


# ---------------- DELETE PICKLE (ADMIN ONLY) ---------------- #

@router.delete("/delete/{pickle_id}", dependencies=[Depends(require_admin)])
async def delete_pickle(pickle_id: str):
    result = db.pickles.delete_one({"_id": ObjectId(pickle_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Pickle not found")

    return {"message": "Pickle deleted successfully"}


# ---------------- LIST PICKLES (PUBLIC) ---------------- #

@router.get("/list/")
def list_pickles():
    pickles = list(db.pickles.find())

    # Convert ObjectId → string for frontend
    for p in pickles:
        p["_id"] = str(p["_id"])

    return pickles
