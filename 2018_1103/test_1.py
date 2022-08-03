from machine import Pin, Timer
led=Pin(2,Pin.OUT)
counter=0

def tt(t):
    global counter
    counter+=1
    print(counter)
    led.value(not led.value())
    if counter==5:
        T1.deinit()
        print('stopped_1')

T1=Timer(-1)
T1.init(period=1000, mode=Timer.PERIODIC, callback=tt)
#T1.init(period=1000, mode=Timer.ONE_SHOT, callback=tt)
