from typing import Optional
from pydantic import BaseModel

class Stores(BaseModel):
    drink_names: str
    prices: str
    ratings: str
    store_names: str
    address: str

class StoresCount(BaseModel):
    total: int