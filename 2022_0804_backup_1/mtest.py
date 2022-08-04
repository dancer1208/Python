import bigSymbol
from machine import Pin, I2C
import ssd1306
import dht
import time

d = dht.DHT11(Pin(13))
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
dsp = bigSymbol.Symbol(oled)
dsp.clear()
dsp.temp(0, 18)
dsp.humid(0, 38)


def DHT11():
    d.measure()
    temp = d.temperature()
    hum  = d.humidity()
    t = '{}c'.format(temp)
    h = '{}%'.format(hum)
    print('\u6eab\u5ea6:{}\u00b0C'.format(temp))
    print('\u6fd5\u5ea6:{}%'.format(hum))
    print('')
    return (t, h)

def main():
    while True:
            temp, hum = DHT11()
            dsp.text(temp, 34, 18)
            dsp.text(hum, 34, 38)
            oled.show()
            time.sleep(5)

main()
