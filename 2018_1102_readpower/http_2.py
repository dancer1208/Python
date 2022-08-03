import urllib.request

x = urllib.request.urlopen('http://192.168.0.100:1234/')
#x = urllib.request.urlopen('http://www.google.com')
x_str=bytes.decode(x.read())
print(x_str)
#print(x.read())
