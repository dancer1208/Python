print('----- Main.py starts from  Dancer','\r\n')

import funs,urandom
from funs import flash
from machine import Timer
import socket
from machine import Pin

# funs.connectAP('dancer_619','13572468')
funs.connectAP('Dancer14-13','12081208')
print('----- STA is connected from  Dancer','\r\n')
funs.flash(5)

httpHeader = funs.get_httpHeader()
PORT=1234
print("Start running Website ")

#from machine import Pin
LED0 = Pin(5, Pin.OUT)
LED1 = Pin(4, Pin.OUT)
LED2 = Pin(0, Pin.OUT)
LED0.value(1)
LED1.value(1)
LED2.value(1)

# with open('data.txt','r') as f:
#     num_s=f.read()
#     num=int(num_s)
#     print('目前共有 ',num_s,'人次測試過')
#f.close()

n1=0
n2=0
tt=[0,0,0,0,0,0,0,0]
temp=0
hum=0
colorGB1 = '#3c99dc'
colorGB2 = '#3c00dc'
s=socket.socket()
HOST='0.0.0.0'
    
#    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(30)
print("Server port",PORT)

while True:
    client,addr=s.accept()
    yy=client.settimeout(3.0)
    try:
        req=client.recv(512)
#            temp, hum = DHT11()
        tt=funs.readntp()
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
    print(LEDON0,LEDON2,LEDOFF0)
    if LEDON0 == 6:
        n1=n1+1
        funs.flash(1)
        timer=Timer(-1)
        timer.init(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:funs.flash(5))
        colorGB1 = '#'+str(999999-urandom.getrandbits(19))
    if LEDON2 == 6:
        n1=n1+1
        funs.flash(2)
        timer=Timer(-1)
        timer.init(period=10000, mode=Timer.ONE_SHOT, callback=lambda t:funs.flash(10))
        colorGB2 = '#'+str(999999-urandom.getrandbits(19))
    if LEDOFF0 == 6:
        LED2.value(0)
        time.sleep(0.1)
        LED2.value(1)
        n1=n1+1
        funs.flash(3)

    n2+=1
    client.send(httpHeader.format(n2=n2,n1=n1,temp=temp,hum=hum,colorGB1=colorGB1,colorGB2=colorGB2,
    t0=tt[0],t1=tt[1],t2=tt[2],t3=tt[3]+8,t4=tt[4],t5=tt[5]))
    client.close()
    print(n2,'-'*40)

