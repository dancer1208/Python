import esp,gc,webrepl,time,network,ntptime
esp.osdebug(None)
gc.collect()
from machine import Pin, Timer

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
        <title>MicroPython</title>
        <script src="script.js" async></script>
      </head>
      <body>
        <h1 style="text-align:center;color:blue;">2022_0904</h1>
        <h3 id="ppp"></h3>   
        <p><b><h1 align="center"> 武男的_L0220_通信網路技術實驗室鐵捲門</h1></b></p>
        <p><b><h1 align="center">連線{n2}次，啟閉{n1}次，目前時間{t0}年{t1}月{t2}日{t3}時{t4}分{t5}秒</h1></b></p>
        <form align="center">
        <button name="Up" value="ON001" type="submit"
        style="width:400px;height:100px;font-size:40px;color:red;background:{colorGB1}">計時5秒</button><br><br>
        <button name="Stop" value="ON001" type="submit"
        style="width:400px;height:100px;font-size:40px;color:red;background:{colorGB2}">計時10秒</button><br><br>
        <button name="Down" value="ON001" type="submit"
        style="width:400px;height:100px;font-size:40px;color:red;background:#66d3fa">下</button>
        </form>

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

def readntp():
    t_ntp=[0,0,0,0,0,0,0,0]
    t=ntptime.time()
    t_tuple=time.localtime(t)
    time.sleep(0.5)
    t_ntp[0:7]=t_tuple[0:7]
    return(t_ntp)
    
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


