from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:airflow@localhost:3306/FOODY")

meta = MetaData()

conn = engine.connect()