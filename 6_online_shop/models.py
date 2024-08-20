from pydantic import BaseModel, Field
from typing import Optional


class UserIn(BaseModel):
    name: str = Field(max_length=50)
    surname: str = Field(max_length=50)
    email: str = Field(max_length=128)
    password: str = Field(max_length=128)


class UserOut(BaseModel):
    id: int
    name: str
    surname: str
    email: str


class ProductIn(BaseModel):
    name: str = Field(max_length=100)
    description: Optional[str] = None
    price: float


class ProductOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float


class OrderIn(BaseModel):
    user_id: int
    product_id: int
    order_date: str
    status: str


class OrderOut(BaseModel):
    id: int
    user_id: int
    product_id: int
    order_date: str
    status: str