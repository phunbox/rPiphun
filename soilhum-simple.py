import RPi.GPIO as GPIO
import time
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)

while True:
    i=GPIO.input(27)
    if i==0:
        print "mokro"
        time.sleep(1.0)

    elif i==1:
        print "sucho"
        time.sleep(1.0)
#    print i

