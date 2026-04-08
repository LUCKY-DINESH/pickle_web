from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import users, pickles   # routers folder
from . import orders                  # orders.py in backend folder

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(pickles.router, prefix="/pickles", tags=["Pickles"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])
