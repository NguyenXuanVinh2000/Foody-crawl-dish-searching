from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine


stores = Table(
    "store",
    meta,
    Column("drink_names", String(225)),
    Column("prices",Integer),
    Column("statuss", String(255)),
    Column("ratings", String(255)),
    Column("store_names", String(3)),
    Column("address", String(255)),

)

meta.create_all(engine)