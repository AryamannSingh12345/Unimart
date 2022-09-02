#!/usr/bin/python

from websocket import create_connection
import sys
import requests

ws = create_connection("wss://service.codechallenge.co.uk/socket")
ws.send('connect|{"teamName":"Tremendous Three","password":"Rivich"}')
result1 =  ws.recv()
ws.send("matchlivegoals|")
link = ws.recv()

home = 0
away = 0

data = requests.get(link[15::]).text
for line in data:
     if "home" in line:
         ws.send("matchlivegoals|goal|home")
     elif "away" in line:
         ws.send("matchlivegoals|goal|away")

result2 = ws.recv()

print("Received '%s'" % result2)

ws.close()