import mysql.connector

MYSQL_HOST = "172.17.0.1"
MYSQL_DB = "FOODY"
MYSQL_TABLE = "store"
MYSQL_USER ="root"
MYSQL_PASSWORD = "airflow"
MYSQL_PORT = 3306
MYSQL_UPSERT = False
MYSQL_RETRIES = 3
MYSQL_CLOSE_ON_ERROR = True
MYSQL_CHARSET = 'utf-8'

mydb = mysql.connector.connect(
  host=MYSQL_HOST,
  user=MYSQL_USER,
  password=MYSQL_PASSWORD,
  database=MYSQL_DB
)


def check_data(drink_name, store_name):
    new_data = (drink_name, store_name)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT drink_names, store_names FROM store")
    myresult = mycursor.fetchall()
    for x in myresult:
        if x == new_data:
            return True
    return False
