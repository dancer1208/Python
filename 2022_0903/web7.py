import time, gc, socket,ntptime,dht,urandom
from machine import Pin
from machine import Timer
temp=0
hum=0
tt=[0,0,0,0,0,0,0,0]
d=dht.DHT11(Pin(13))
led = Pin(2,Pin.OUT)

def flash(times):
    led = Pin(2,Pin.OUT)

    for i in range(times):
        led.value(not led.value())
        time.sleep(0.1)
        led.value(not led.value())
        time.sleep(0.1)

def readntp():
    t_ntp=[0,0,0,0,0,0,0,0]
    t=ntptime.time()
    t_tuple=time.localtime(t)
    time.sleep(0.5)
    t_ntp[0:7]=t_tuple[0:7]
    return(t_ntp)

def DHT11():
    d.measure()
    temp=d.temperature()
    hum=d.humidity()
    print('溫度:{}\u00b0C'.format(temp))
    print('濕度:{}%'.format(hum))
    print('')
    return(temp,hum)

# def changeBGcolor():
#     colorGB1 = '#123456'
#     colorGB2 = '#3c00dc'
#     flash(5)
#     client.send(httpHeader.format(n2=n2,n1=n1,temp=temp,hum=hum,colorGB1=colorGB1,colorGB2=colorGB2,
#     t0=tt[0],t1=tt[1],t2=tt[2],t3=tt[3]+8,t4=tt[4],t5=tt[5]))

def url(PORT):
    import socket
    LED0 = Pin(5, Pin.OUT)
    LED1 = Pin(4, Pin.OUT)
    LED2 = Pin(0, Pin.OUT)
    LED0.value(1)
    LED1.value(1)
    LED2.value(1)
    n1=0
    n2=0
    tt=[0,0,0,0,0,0,0,0]
    temp=0
    hum=0
    colorGB1 = '#3c99dc'
    colorGB2 = '#3c00dc'
    s=socket.socket()
    HOST='0.0.0.0'
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
        <h1>2000_0805</h1>
        <button style="width:200px; height:50px; background:aqua; font-size:large" onclick="document.getElementById('ppp').innerHTML='just test'">clickme</button>
        <h3 id="ppp"></h3>   
        <p><b><h1 align="center"> 武男的_L0220_通信網路技術實驗室鐵捲門</h1></b></p>
        <p><b><h1 align="center">連線{n2}次，啟閉{n1}次，目前時間{t0}年{t1}月{t2}日{t3}時{t4}分{t5}秒</h1></b></p>
        <form align="center">
        <button name="Up" value="ON001" type="submit"
        style="width:400px;height:100px;font-size:40px;color:red;background:{colorGB1}">計時5秒</button><br><br>
        <button name="Stop" value="ON001" type="submit"
        style="width:400px;height:100px;font-size:40px;color:red;background:{colorGB2}">計時3秒</button><br><br>
        <button name="Down" value="ON001" type="submit"
        style="width:400px;height:100px;font-size:40px;color:red;background:#66d3fa">下</button>
        </form>

      </body>
    </html>
    """
        # <script>
        #     function alertTest(){
        #         alert('just a test');
        # } 
        # </script>
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(30)

    while True:
        client,addr=s.accept()

        yy=client.settimeout(3.0)
        try:
            req=client.recv(512)
#            temp, hum = DHT11()
            tt=readntp()
            print(tt)
            time.sleep(0.1)
            gc.collect()
        except OSError:
            print(yy,' Oops! Timeout happened')
            gc.collect()
            req=0
            client,addr=s.accept()

        request = str(req)
        req=0
        LEDON0 = request.find('/?Up=ON001')
        LEDON2 = request.find('/?Stop=ON001')
        LEDOFF0 = request.find('/?Down=ON001')
        if LEDON0 == 6:
            # LED0.value(0)
            # time.sleep(0.1)
            # LED0.value(1)
            n1=n1+1
            flash(1)
            # time.sleep(5)
            timer=Timer(-1)
            timer.init(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:flash(5))
            colorGB1 = '#'+str(999999-urandom.getrandbits(19))
            # colorGB2 = '#3c00dc'
            # flash(3)
        if LEDON2 == 6:
            # LED1.value(0)
            # time.sleep(0.1)
            # LED1.value(1)
            n1=n1+1
            flash(2)
            # colorGB2 = '#654321'
            # colorGB1 = '#3c99dc'
            # time.sleep(3)
            timer=Timer(-1)
            timer.init(period=10000, mode=Timer.ONE_SHOT, callback=lambda t:flash(10))
            colorGB2 = '#'+str(999999-urandom.getrandbits(19))

            # flash(3)
        if LEDOFF0 == 6:
            LED2.value(0)
            time.sleep(0.1)
            LED2.value(1)
            n1=n1+1
            flash(3)

        n2+=1
        client.send(httpHeader.format(n2=n2,n1=n1,temp=temp,hum=hum,colorGB1=colorGB1,colorGB2=colorGB2,
        t0=tt[0],t1=tt[1],t2=tt[2],t3=tt[3]+8,t4=tt[4],t5=tt[5]))
        client.close()
        print(n2,'-'*40)
