import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883)

while True:
    light = random.choice(["ON", "OFF"])
    fan = random.choice(["ON", "OFF"])
    temp = round(random.uniform(20, 40), 2)

    client.publish("sensor/light", light)
    client.publish("sensor/fan", fan)
    client.publish("sensor/temp", temp)

    print(light, fan, temp)
    time.sleep(5)