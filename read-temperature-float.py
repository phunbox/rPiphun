#!/usr/bin/python
import sys
import Adafruit_DHT
import socket
import time

#while True:
humidity, temperature = Adafruit_DHT.read_retry(22, 4)
timestamp = int(time.time())
inttemp = float(temperature)
inthum = float(humidity)
print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
sock = socket.socket()
sock.connect(("127.0.0.1",2003))
sock.sendall("test.temp2 %d %d\n" % (inttemp, timestamp))
sock.close
sock1 = socket.socket()
sock1.connect(("127.0.0.1",2003))
sock1.sendall("test.wilgoc2 %d %d\n" % (inthum, timestamp))

sock1.close
print "teraz"
print inthum
print inttemp
