import urllib.request

x = urllib.request.urlopen('https://www.ctbcbank.com/CTCBPortalWeb/appmanager/ebank/rb')
#x = urllib.request.urlopen('http://www.google.com')
x_str=bytes.decode(x.read())
p1,p2=x_str.split('匯率查詢',2)
#print(p2)
p21,p22=p1.split('客戶投資現值查詢',2)
print(p21)
#print(x.read())
