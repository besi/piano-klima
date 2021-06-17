import machine
import time

green_pin = 25
yellow_pin = 26
red_pin = 27

red = machine.Pin(red_pin, machine.Pin.OUT)
green = machine.Pin(green_pin, machine.Pin.OUT)
yellow = machine.Pin(yellow_pin, machine.Pin.OUT)

while True:
    v = 1
    red.value(v)
    yellow.value(1-v)
    green.value(v)
    time.sleep(1)
    red.value(1-v)
    yellow.value(v)
    green.value(1-v)
    time.sleep(1)


