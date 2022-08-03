import urllib.request

x = urllib.request.urlopen('https://www.ctbcbank.com/CTCBPortalWeb/appmanager/ebank/rb')
#x = urllib.request.urlopen('http://www.google.com')
x_str=bytes.decode(x.read())
print(x_str)
#print(x.read())
