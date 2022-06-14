from fastapi import APIRouter
from config.db import conn
from models.store import stores
from schemas.store import Stores, StoresCount
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select
from sqlalchemy import and_

from cryptography.fernet import Fernet

drinks = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)

@drinks.get("/drinks/all", tags=["drinks"], response_model=List[Stores],  description="Show all drink in database",
)
def get_all_drinks():
    return conn.execute(stores.select()).fetchall()


@drinks.get("/drinks/count", tags=["drinks"], response_model=StoresCount,  description="Total drink in database",
)
def get_drinks_count():
    result = conn.execute(select([func.count()]).select_from(stores))
    return {"total": tuple(result)[0][0]}



@drinks.get(
    "/drinks",
    tags=["drinks"],
    response_model=List[Stores],
    description="Get a list of all drinks of the store",
)
def get_stores(store_names: str):
    return conn.execute(stores.select().where(stores.c.store_names == store_names)).fetchall()



@drinks.get(
    "/drinks/{drink_names}",
    tags=["drinks"],
    response_model=List[Stores],
    description="Get a dink in stores",
)
def get_drinks(drink_names: str):
    return conn.execute(stores.select().where(stores.c.drink_names == drink_names)).fetchall()

@drinks.get(
    "/drinks/select/{drink_names}_{store_names}",
    tags=["drinks"],
    response_model=Stores,
    description="Get drink of store",
)
def get_drink(drink_names: str, store_names: str):
    return conn.execute(stores.select().where(stores.c.store_names == store_names).where(stores.c.drink_names == drink_names)).first()


@drinks.post("/drinks", tags=["drinks"], response_model=Stores, description="Create a new drinks")
def create_drinks(drink: Stores):
    new_drink = {"drink_names": drink.drink_names, "prices": drink.prices, "ratings": drink.ratings, "store_names": drink.store_names, "address": drink.address }
    result = conn.execute(stores.insert().values(new_drink))
    return conn.execute(stores.select().where(stores.c.drink_names == result.lastrowid)).first()


@drinks.put("drinks/update/{drink_names}_{store_names}", tags=["drinks"], response_model=Stores, description="Update a drinks by drink_names, store_names")
def update_drinks(drink: Stores, drink_names: str, store_names: str):
    new_drink = {"drink_names": drink.drink_names, "prices": drink.prices, "ratings": drink.ratings, "store_names": drink.store_names, "address": drink.address }
    conn.execute(stores.update().values(new_drink).where(stores.c.store_names == store_names).where(stores.c.drink_names == drink_names))
    return None


# @drinks.delete("/drink_names, store_names", tags=["drinks"], status_code=HTTP_204_NO_CONTENT)
# def delete_drinks(drink_names: str,store_names: str ):
#     conn.execute(stores.delete().where(stores.c.drink_names == drink_names and stores.c.store_names == store_names))
#     return conn.execute(stores.select().where(stores.c.drink_names == drink_names)).first()


