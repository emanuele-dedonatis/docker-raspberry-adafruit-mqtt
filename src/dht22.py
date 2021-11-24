import adafruit_dht,board
import paho.mqtt.client as mqtt
import sys,time

INTERVAL_SEC = 60*20
MQTT_USERNAME = "username"
MQTT_PASSWORD = "password"
MQTT_URL = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "rpi/dht22"

try:
	client = mqtt.Client()
	dhtDevice = adafruit_dht.DHT22(board.D4)
except Exception as e:
	print(e)

while True:
    try:
        client.username_pw_set(username=MQTT_USERNAME,password=MQTT_PASSWORD)
        client.connect(MQTT_URL, MQTT_PORT)
        humidity = dhtDevice.humidity
        temperature = dhtDevice.temperature
        msg = '{{"t":{0:0.1f},"h":{1:0.1f}}}'.format(temperature, humidity)
        client.publish(MQTT_TOPIC,msg)
        print(msg)
    except Exception as e:
        print(e)

    sys.stdout.flush()
    time.sleep(INTERVAL_SEC)
