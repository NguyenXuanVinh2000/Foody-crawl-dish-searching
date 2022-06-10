from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:airflow@172.17.0.1:3306/FOODY")

meta = MetaData()

conn = engine.connect()