import time
from machine import Pin
def aaa(times):
    Led = Pin(2,Pin.OUT)

    for i in range(times):
        Led(0)
        time.sleep(1)
        Led(1)
        time.sleep(0.5)

def bbb(times):
    Led = Pin(2,Pin.OUT)

    for i in range(times):
        Led(0)
        time.sleep(0.5)
        Led(1)
        time.sleep(0.5)

aaa(5)
bbb(3)
