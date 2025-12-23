import paho.mqtt.client as mqtt
import mysql.connector
from datetime import datetime

light_status = "OFF"
fan_status = "OFF"
temperature = 0.0

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iot_application"
)
cursor = db.cursor()

def on_message(client, userdata, msg):
    global light_status, fan_status, temperature

    topic = msg.topic
    value = msg.payload.decode()

    if topic == "sensor/light":
        light_status = value
    elif topic == "sensor/fan":
        fan_status = value
    elif topic == "sensor/temp":
        temperature = float(value)

    cursor.execute(
        "INSERT INTO smart_home_status(light_status, fan_status, temperature, date_time) VALUES (%s,%s,%s,%s)",
        (light_status, fan_status, temperature, datetime.now())
    )
    db.commit()

    print("Data Stored:", light_status, fan_status, temperature)

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883)

client.subscribe("sensor/light")
client.subscribe("sensor/fan")
client.subscribe("sensor/temp")

client.on_message = on_message
client.loop_forever()