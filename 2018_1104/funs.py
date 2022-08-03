import esp
esp.osdebug(None)
import gc
import webrepl
#webrepl.start()
gc.collect()
from machine import Pin, Timer
import time
import network
#global counter
counter=0
def count_0(flashes):
    from machine import Pin, Timer, reset
    led=Pin(2,Pin.OUT)
#    counter=0
    def tt(t):
        global counter
        counter+=1
        print(counter)
        led.value(not led.value())
        if counter==flashes:
            T1.deinit()
#            print(flashes, 'stopped')
            reset()

    T1=Timer(-1)
    T1.init(period=1000, mode=Timer.PERIODIC, callback=tt)

def tim_2():
    from machine import Pin, Timer
    led=Pin(2,Pin.OUT)
    counter=0

    def tt(t):
        global counter
        counter+=1
        print(counter)
        led.value(not led.value())
        if counter==10:
            T1.deinit()
            print('stopped')

    T1=Timer(-1)
    T1.init(period=1000, mode=Timer.PERIODIC, callback=tt)


def tim_1():
    from machine import Timer
    led=Pin(2,Pin.OUT)
    tim=Timer(-1)
    tim.init(period=100, mode=Timer.PERIODIC, callback=lambda t:led.value(not led.value()))
    try:
        while True:
            pass
    except:
        tim.deinit()
        led.value(0)
        print('stopped')



def readDHT11(pin):
    import dht
    d=dht.DHT11(Pin(pin))
    d.measure()
    t='{:02}\u00b0c'.format(d.temperature())
    h='{:02}%'.format(d.humidity())
#    t=d.temperature()
#    h=d.humidity()
    return(t,h)

def get_httpHeader():
    httpHeader = b"""\
    HTTP/1.0 200 OK

    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Micropython</title>
      </head>
      <body>
        <div style="border:2px orange solid;margin:0px auto;text-align:center;background-color:rgb(232,106,192)">
        <p><b><h1>歡迎光臨 Dancer 的測試網站</h1></b></p>
        <p><b><h1>  {mem} 8266LED燈測試，總共{num}人按過喔</h1></b></p>
        <p><b><h1>8266 RSSI測試，目前功率強度：dBm{rssi}dBm</h1></b></p>
        </div>
            <div style="border:5px orange solid;width:400 height:400;
            border-style:double;border-width:10px;text-align:left;background-color:rgb(240,220,192)">
            <span style="font-size:2.2cm;">
            　　　　　ＥＤＣＢＡ<br>
            ＭＮＯＰＧＲＳＴＵＶ<br>
            </span><br>
            </div>
        </body>
    </html>
    """
    return(httpHeader)

def check_RSSI(essid):
    import network
    wlan = network.WLAN(network.STA_IF)
    wifi= wlan.scan()
    print('\r\n')
    for sta in wifi:
        sta_name=bytes.decode(sta[0])
        sta_pwr=sta[3]
        sta_mac_bytes=sta[1]
        sta_mac_str=''
        for b in sta_mac_bytes:
            sta_mac_str += "%02x" % b
        if essid in sta_name:
            print('ssid:',sta_name,', mac:',sta_mac_str,', RSSI:',sta_pwr,'dBm')
            return(sta_pwr)
    
def flash(times):
    led = Pin(2,Pin.OUT)

    for i in range(times):
        led.value(not led.value())
        time.sleep(0.1)
        led.value(not led.value())
        time.sleep(0.1)

    led.value(0)
    
def connectAP(ssid,pwd):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid,pwd)
        while not wlan.isconnected():
            pass
    print('network config:',wlan.ifconfig())

print('-----funs.py is imported by Dancer')


