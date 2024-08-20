from fastapi import APIRouter, HTTPException
from sqlalchemy import Table, Column, Integer, String, MetaData
from database import database, metadata
from models import UserIn, UserOut

user_router = APIRouter()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("surname", String),
    Column("email", String),
    Column("password", String)
)


@user_router.post("/", response_model=UserOut)
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name, surname=user.surname, email=user.email, password=user.password)
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@user_router.get("/", response_model=list[UserOut])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)