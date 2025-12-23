import paho.mqtt.client as mqtt
import mysql.connector
from datetime import datetime

pulse = 0
spo2 = 0

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iot_application"
)
cursor = db.cursor()

def on_message(client, userdata, msg):
    global pulse, spo2

    if msg.topic == "health/pulse":
        pulse = int(msg.payload.decode())
    elif msg.topic == "health/spo2":
        spo2 = int(msg.payload.decode())

    cursor.execute(
        "INSERT INTO health_data(pulse,spo2,timestamp) VALUES(%s,%s,%s)",
        (pulse, spo2, datetime.now())
    )
    db.commit()

    if pulse > 100 or spo2 < 95:
        print("🚨 ALERT: Patient Condition Critical")
        print("Pulse:", pulse, "SpO2:", spo2)

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883)

client.subscribe("health/pulse")
client.subscribe("health/spo2")
client.on_message = on_message

client.loop_forever()