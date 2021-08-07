#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
def reading(sensor):
    import time
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False)
     
    GPIO.setmode(GPIO.BOARD)
    TRIG = 11
    ECHO = 13
     
    if sensor == 0:
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(0.3)
        #トリガを10µsハイにする
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        signaloff = time.time()
        signalon = time.time()
        #ECHOがHIGHになる時刻を計測
        while GPIO.input(ECHO) == 0:
          signaloff = time.time()
        #ECHOがLOWになる時刻を計測
        while GPIO.input(ECHO) == 1:
          signalon = time.time()
 
        timepassed = signalon - signaloff
        distance = timepassed * 17000
        return distance
        GPIO.cleanup()
    else:
        print ("Incorrect usonic() function varible.")
         
for _ in range(100):
    print (reading(0))
