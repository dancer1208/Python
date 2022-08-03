import time
import ntptime
def kk():
    t=ntptime.time()
    tt=time.localtime(t)
    print(tt)
while True:
    kk()
