from fastapi import APIRouter
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData
from database import database, metadata
from models import OrderIn, OrderOut

order_router = APIRouter()

orders = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("product_id", Integer, ForeignKey("products.id")),
    Column("order_date", String),
    Column("status", String)
)


@order_router.post("/", response_model=OrderOut)
async def create_order(order: OrderIn):
    query = orders.insert().values(user_id=order.user_id, product_id=order.product_id, order_date=order.order_date, status=order.status)
    last_record_id = await database.execute(query)
    return {**order.dict(), "id": last_record_id}


@order_router.get("/", response_model=list[OrderOut])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)