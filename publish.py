import paho.mqtt.client as mqtt
from random import randrange
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)
i=0
while i<10:
    randNumber = randrange(20,40)
    string="Good Morning"
    chr='M'
    client.publish("TEMPERATURE", randNumber)
    client.publish("Greetings",string)
    client.publish("Character",chr)
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    print("Just published " + string + " to Topic Greetings")
    print("Just published " + chr + " to Topic Character")
    time.sleep(1)
    i=i+1
