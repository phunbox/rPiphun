import RPi.GPIO as GPIO
import time
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)         #Read output from PIR motion sensor
while True:
       i=GPIO.input(17)
       if i==0:                 #When output from motion sensor is LOW
             print "Gitareczka."
             time.sleep(0.5)
       elif i==1:               #When output from motion sensor is HIGH
             print "Jest ruch."
             time.sleep(0.5)
