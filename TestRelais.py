import machine
import time

humid_pin = 17
dehumid_pin = 16

humid = machine.Pin(humid_pin, machine.Pin.OUT)
dehumid = machine.Pin(dehumid_pin, machine.Pin.OUT)

while True:
    v = 1
    humid.value(v)
    dehumid.value(1-v)
    time.sleep(3)
    humid.value(1-v)
    dehumid.value(v)
    time.sleep(3)

