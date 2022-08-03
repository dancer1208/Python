from machine import Pin, Timer
led=Pin(2,Pin.OUT)
T1=Timer(-1)
T1.init(period=1000, mode=Timer.PERIODIC, callback=lambda tt:led.value(not led.value()))
try:
    while True:
        pass
except:
    T1.deinit()
    led.value(0)
    print('stopped')
