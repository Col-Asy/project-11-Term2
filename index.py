"""Imports"""
from math import floor
import json
import time
from window import screen_break
config_file = open('./config.json')
config = json.load(config_file)


"""# A small peice of code to send a push 
notification that the script has started"""
while True:
    print("Index loop interations")
    time.sleep(config["active"]*60)
    screen_break(int(floor(config["sleep"])))