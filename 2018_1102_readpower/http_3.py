import urllib.request
x = urllib.request.urlopen('http://124.218.93.176:7070')
#x_read=x.read()
x_str=bytes.decode(x.read())
print(x_str)
#print(x_bytes)
#print(rssi)
#print(x.read())
#print(x_str)
