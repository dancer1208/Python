import time, gc, socket
from machine import Pin
def flash(times):
    led = Pin(2,Pin.OUT)

    for i in range(times):
        led.value(not led.value())
        time.sleep(0.1)
        led.value(not led.value())
        time.sleep(0.1)

def url(PORT):
#    import time
    print("Running website ")
#    import socket
#    from machine import Pin
    LED0 = Pin(5, Pin.OUT)
    LED1 = Pin(4, Pin.OUT)
    LED2 = Pin(0, Pin.OUT)
    LED0.value(1)
    LED1.value(1)
    LED2.value(1)
    num = 0
#    test=0
    s=socket.socket()
    HOST='0.0.0.0'
    httpHeader = b"""\
    HTTP/1.0 200 OK

    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>MicroPython</title>
      </head>
      <body>
        <p><b><h1 align="center">歡迎光臨 武男 的測試網站</h1></b></p>
        <p><b><h1 align="center">ESP8266 控制鐵捲門 測試</h1></b></p>
        <p><b><h1 align="center">總共{num}人按過喔</h1></b></p>
        <form align="center">
        <button name="Up" value="ON001" type="submit"
        style="width:400px;height:100px;font-size:40px;color:red;background:#3c99dc">上</button><br><br>
        <button name="Stop" value="ON001" type="submit"
        style="width:400px;height:100px;font-size:40px;color:red;background:#d5f3fe">停</button><br><br>
        <button name="Down" value="ON001" type="submit"
        style="width:400px;height:100px;font-size:40px;color:red;background:#66d3fa">下</button>
        </form>
      </body>
    </html>
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(30)
    print("Server port",PORT)

    while True:
        client,addr=s.accept()
        print("Client address:",addr)
        
        yy=client.settimeout(3.0)
#        print(yy)
        try:
            print(yy,' lucky')
            req=client.recv(2048)
        except OSError:
            print(yy,' Oops! Timeout happened')
            gc.collect()
            client,addr=s.accept()

        print(req)
        request = str(req)
        req==0
        LEDON0 = request.find('/?Up=ON001')
        LEDON2 = request.find('/?Stop=ON001')
        LEDOFF0 = request.find('/?Down=ON001')
        print('LEDON0=',LEDON0)
        print('LEDON2=',LEDON2)
        print('LEDOFF0=',LEDOFF0)
        if LEDON0 == 6:
            LED0.value(0)
            time.sleep(0.1)
            LED0.value(1)
            num=num+1
            flash(1)
        if LEDON2 == 6:
            LED1.value(0)
            time.sleep(0.1)
            LED1.value(1)
            num=num+1
            flash(2)
        if LEDOFF0 == 6:
            LED2.value(0)
            time.sleep(0.1)
            LED2.value(1)
            num=num+1
            flash(3)
       
        client.send(httpHeader.format(num=num))
        client.close()
#        test=num
        print('-'*40)


