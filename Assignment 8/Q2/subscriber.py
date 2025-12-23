import paho.mqtt.client as mqtt
import mysql.connector
from datetime import datetime

light_status = "OFF"
fan_status = "OFF"
temperature = 0.0   # not used here

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
   database="iot_application"
)
cursor = db.cursor()

def on_message(client, userdata, msg):
    global light_status, fan_status

    command = msg.payload.decode()

    if msg.topic == "home/light":
        light_status = command
    elif msg.topic == "home/fan":
        fan_status = command

    cursor.execute(
        "INSERT INTO smart_home_status(light_status, fan_status, temperature, date_time) VALUES (%s,%s,%s,%s)",
        (light_status, fan_status, temperature, datetime.now())
    )
    db.commit()

    print("Updated:", light_status, fan_status)

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883)

client.subscribe("home/light")
client.subscribe("home/fan")
client.on_message = on_message

client.loop_forever()