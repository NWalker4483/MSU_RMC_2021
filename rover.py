#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import serial
import time

def on_connect(client, userdata, flags, rc):
    client.subscribe("A")
    client.subscribe("B")
    client.subscribe("C")
    client.subscribe("D")
    print('Connected with result code ' + str(rc))

def on_message(client, userdata, msg):
    global ser
    data = msg.payload.decode().rjust(4)
    if msg.topic == "A":
        ser.write(bytes('A{0}'.format(data)))
        
    elif msg.topic == "B":
        ser.write(bytes('B{0}'.format(data)))

    elif msg.topic == "C":
        ser.write(bytes('C{0}'.format(data)))

    elif msg.topic == "D":
        ser.write(bytes('D{0}'.format(data)))


client = mqtt.Client()
client.connect('localhost', 1883, 60)

client.on_connect = on_connect
client.on_message = on_message
class A():
    def write(self,data):
        print(data)
ser = serial.Serial("/dev/arduino_uno", 9600)

client.loop_forever()