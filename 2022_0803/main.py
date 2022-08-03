print('----- Main.py starts from  Dancer','\r\n')

import funs
import socket
from machine import Pin

funs.connectAP('dancer_619','13572468')
print('----- STA is connected from  Dancer','\r\n')
funs.flash(5)

httpHeader = funs.get_httpHeader()
PORT=1234
print("Start running Website ")

#from machine import Pin
LED0 = Pin(0, Pin.OUT)
LED2 = Pin(2, Pin.OUT)

with open('data.txt','r') as f:
    num_s=f.read()
    num=int(num_s)
    print('目前共有 ',num_s,'人次測試過')

#f.close()
color1='pink'
color2='pink'
s=socket.socket()
HOST='0.0.0.0'
    
#    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(30)
print("Server port",PORT)

global counter
counter=0
#funs.count_0(300)

while True:
    client,addr=s.accept()
    num=num+1
    mem=gc.mem_free()
        
    print("Client address:",mem)
        
    try:
        req=client.recv(512)
        request = str(req)
    except:
        print('error happened')
#        machine.reset()
        
    rssi=funs.check_RSSI('uPY')
#    rssi=0
#    print("Request:")
#    print(req)
    request = str(req)
    LEDON0 = request.find('/?FLS=FLS1')
    LEDON2 = request.find('/?LED=ON2')
    LEDOFF0 = request.find('/?FLS=FLS3')
    LEDOFF2 = request.find('/?LED=OFF2')
    print('LEDON0=',LEDON0)
    print('LEDON2=',LEDON2)
    print('LEDOFF0=',LEDOFF0)
    print('LEDOFF2=',LEDOFF2)
    if LEDON0 == 6:
        funs.flash(1)
        num=num+1
    if LEDON2 == 6:
        LED2.value(0)
        num=num+1
    if LEDOFF0 == 6:
        funs.flash(2)
        num=num+1
    if LEDOFF2 == 6:
        LED2.value(1)
        num=num+1

    with open('data.txt','w') as f:
        num_s=str(num)
        f.write(num_s)
    #f.close()
#        print(request)
#    client.send(httpHeader.format(temp=temp,hud=hud,mem=mem,num=num,rssi=rssi,color1=color1,color2=color2))
    client.send(httpHeader.format(mem=mem,num=num,rssi=rssi,color1=color1,color2=color2))
    client.close()

