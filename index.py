"""Imports"""
from math import floor
import json
import time
from window import screen_break
# from gui_time import change_time
from welcome import welcome_screen

config_file = open('./config.json')
config = json.load(config_file)

welcome_screen(config)

while True:
    print(config)
    print("Index loop interations")
    time.sleep(config["active"]*60)
    screen_break(int(floor(config["sleep"])))
