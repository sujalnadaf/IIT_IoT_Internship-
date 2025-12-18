# import mysql connector
import mysql.connector
import time
from datetime import datetime

# establish connection with mysql server
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_data",
    use_pure = True
)

# form a query to be executed
id = int(input("Enter id : "))
temp = float (input("Enter temp : "))
humidity = float(input("Enter humidity : "))
now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
timestamp = formatted_time

query = f"insert into sensor_readings values({id}, '{temp}', '{humidity}', '{timestamp}');"

# create a cursor to execute a query
cursor = connection.cursor()

# execute a query
cursor.execute(query)

# commit your changes on mysql server
connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()

