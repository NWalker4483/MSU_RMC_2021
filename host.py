#!/usr/bin/env python3
import paho.mqtt.client as mqtt  # import the client
import pygame
import time

FPS = 24
pygame.init()
pygame.display.set_caption("Control System")

# Connect to broker
broker_address = "localhost" # 192.168.0.3
client = mqtt.Client("Master")
client.connect(broker_address)

# client.on_connect = on_connect
# client.on_message = on_message

Length, Width, Height = 41.91, 55.88, 30  # cm

# Setup pygame
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

running = True
d_pad_held = [False, False, False, False]
button_held = [False, False]
speed = 25
while running:
    client.loop(timeout=.1)
    # - events -
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                d_pad_held[0] = True
            if event.key == pygame.K_RIGHT:
                d_pad_held[1] = True
            if event.key == pygame.K_UP:
                d_pad_held[2] = True
            if event.key == pygame.K_DOWN:
                d_pad_held[3] = True
            if event.key == pygame.K_LSHIFT:
                speed = 75
            if event.key == pygame.K_a:
                button_held[0] = True
            if event.key == pygame.K_s:
                button_held[1] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                d_pad_held[0] = False
            if event.key == pygame.K_RIGHT:
                d_pad_held[1] = False
            if event.key == pygame.K_UP:
                d_pad_held[2] = False
            if event.key == pygame.K_DOWN:
                d_pad_held[3] = False
            if event.key == pygame.K_LSHIFT:
                speed = 25
            if event.key == pygame.K_a:
                button_held[0] = False
            if event.key == pygame.K_s:
                button_held[1] = False

    if d_pad_held[0]:
        client.publish("A", str(speed)[:4])
        client.publish("B", str(-speed)[:4])
    elif d_pad_held[1]:
        client.publish("A", str(-speed)[:4])
        client.publish("B", str(speed)[:4])
    elif d_pad_held[2]:
        client.publish("A", str(speed)[:4])
        client.publish("B", str(speed)[:4])
    elif d_pad_held[3]:        
        client.publish("A", str(-speed)[:4])
        client.publish("B", str(-speed)[:4])
    else:
        client.publish("A", str(0)[:4])
        client.publish("B", str(0)[:4])

    if button_held[0]:
        client.publish("D", str(-speed)[:4])
    elif button_held[1]:
        client.publish("D", str(speed)[:4])
    else:
        client.publish("D", str(0)[:4])

    # - draws (without updates) -
    screen.fill((255,255,255))
    pygame.display.flip()

    # - constant game speed / FPS -
    clock.tick(FPS)

# - end -
pygame.quit()