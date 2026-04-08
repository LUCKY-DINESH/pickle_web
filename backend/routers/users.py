from fastapi import APIRouter, HTTPException, Form
from ..auth import hash_password, verify_password, create_access_token
from ..database import db

router = APIRouter()

# 🔐 CREATE ADMIN (ONE TIME)
@router.post("/create-admin/")
def create_admin():
    admin = db.users.find_one({"username": "admin"})
    if admin:
        return {"message": "Admin already exists"}

    db.users.insert_one({
        "username": "admin",
        "email": "admin@pickle.com",
        "password": hash_password("admin123"),
        "role": "admin"
    })
    return {"message": "Admin created successfully"}


# 👤 USER SIGNUP
@router.post("/signup/")
def signup(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    if db.users.find_one({"email": email}):
        raise HTTPException(status_code=400, detail="Email already exists")

    db.users.insert_one({
        "username": username,
        "email": email,
        "password": hash_password(password),
        "role": "user"
    })
    return {"message": "User created successfully"}


# 🔑 LOGIN (WORKS FOR ADMIN + USER)
@router.post("/login/")
def login(email: str = Form(None), username: str = Form(None), password: str = Form(...)):
    # Swagger UI natively sends 'username', our frontend sends 'email'. We accept both.
    login_id = email or username
    user = db.users.find_one({"email": login_id})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer", "role": user["role"]}
