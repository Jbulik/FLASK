from fastapi import FastAPI
from database import database, metadata
from user import user_router
from product import product_router
from order import order_router

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(product_router, prefix="/products", tags=["products"])
app.include_router(order_router, prefix="/orders", tags=["orders"])