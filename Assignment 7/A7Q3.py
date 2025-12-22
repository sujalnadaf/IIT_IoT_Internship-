from flask import Flask, request
from datetime import datetime

import mysql.connector as myc

app = Flask(__name__)

# database connection
connection = myc.connect(
    host='127.0.0.1',
        port=3306,
        user='root',
        password='root',
        database='iot_application',
        use_pure=True
)
cursor = connection.cursor()

@app.route('/')
def home():
    return "Smart Home Monitoring System"


@app.post('/smart_home_status')
def update_status():
    light = request.form.get('light_status')   # ON / OFF
    fan = request.form.get('fan_status')       # ON / OFF
    temperature = request.form.get('temperature')
    date_time_str = request.form.get('date_time')
    date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")


    query = f"INSERT INTO smart_home_status VALUES ('{light}', '{fan}', {temperature}, '{date_time}');"

    cursor.execute(query)
    connection.commit()

    return "Home status updated successfully"

# ---------------- GET CURRENT STATUS ----------------
@app.get('/smart_home_status')
def get_status():

    query = "SELECT light_status, fan_status, temperature FROM smart_home_status ORDER BY id DESC LIMIT 1;"

    cursor.execute(query)
    data = cursor.fetchone()

    return f"Light : {data[0]} \n \n Fan : {data[1]} \n \n Temperature : {data[2]} °C"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)