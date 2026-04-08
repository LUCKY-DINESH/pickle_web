from pydantic import BaseModel
from typing import Optional

class UserModel(BaseModel):
    username: str
    email: str
    password: str
    role: str = "user"  # default role

class PickleModel(BaseModel):
    name: str
    category: str  # veg / non-veg
    description: str
    price: float
    image_url: str
