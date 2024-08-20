from fastapi import APIRouter
from sqlalchemy import Table, Column, Integer, String, Float, MetaData
from database import database, metadata
from models import ProductIn, ProductOut

product_router = APIRouter()

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String),
    Column("price", Float)
)


@product_router.post("/", response_model=ProductOut)
async def create_product(product: ProductIn):
    query = products.insert().values(name=product.name, description=product.description, price=product.price)
    last_record_id = await database.execute(query)
    return {**product.dict(), "id": last_record_id}


@product_router.get("/", response_model=list[ProductOut])
async def read_products():
    query = products.select()
    return await database.fetch_all(query)