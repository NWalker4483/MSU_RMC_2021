#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import imutils
import time

def on_connect(client, userdata, flags, rc):
    client.subscribe("A")
    client.subscribe("B")
    client.subscribe("C")
    client.subscribe("D")
    print('Connected with result code ' + str(rc))

def on_message(client, userdata, msg):

    if msg.topic == "A":
        print(msg.payload.decode())
    
    elif msg.topic == "B":
        print(msg.payload.decode())

    elif msg.topic == "C":
        print(msg.payload.decode())

    elif msg.topic == "D":
        print(msg.payload.decode())

client = mqtt.Client()
client.connect('localhost', 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

ser = serial.Serial("/dev/arudino_uno", 9600)

# import subprocess
# import cv2
# rtmp_url = "rtmp://127.0.0.1:1935/stream/pupils_trace"

# # In my mac webcamera is 0, also you can set a video file name instead, for example "/home/user/demo.mp4"
# path = 0
# cap = cv2.VideoCapture(path)

# # gather video info to ffmpeg
# fps = int(cap.get(cv2.CAP_PROP_FPS))
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # command and params for ffmpeg
# command = ['ffmpeg',
#            '-y',
#            '-f', 'rawvideo',
#            '-vcodec', 'rawvideo',
#            '-pix_fmt', 'bgr24',
#            '-s', "{}x{}".format(width, height),
#            '-r', str(fps),
#            '-i', '-',
#            '-c:v', 'libx264',
#            '-pix_fmt', 'yuv420p',
#            '-preset', 'ultrafast',
#            '-f', 'flv',
#            rtmp_url]

# # using subprocess and pipe to fetch frame data
# p = subprocess.Popen(command, stdin=subprocess.PIPE)


# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         print("frame read failed")
#         break

#     # YOUR CODE FOR PROCESSING FRAME HERE

#     # write to pipe
#     p.stdin.write(frame.tobytes())