#python3 -m pip install mysql-connector

from dataclasses import dataclass
from sqlite3 import connect
import mysql 
import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost", port = 3306,
                                            database="fin_airflow",
                                            user = "root",
                                            password="Gpsgd@123")

cur = connection.cursor()

#cur.execute("CREATE TABLE testing (testid int)")

cur.execute("SELECT * FROM stcok_data")
results = cur.fetchall()
for x in results:
    print(x)
