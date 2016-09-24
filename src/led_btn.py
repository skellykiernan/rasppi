#!/usr/bin/python
import RPi.GPIO as GPIO
import time


#~### Start of Execution
# uses the Broadcom pins as on the silkscreen of the breakout board
GPIO.setmode(GPIO.BCM) 
ledPin=4
btnPin=17

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Flash on LED to show circuit OK
GPIO.output(ledPin, True)
time.sleep(0.5)
GPIO.output(ledPin, False)

try:
    while True:
        btnState = GPIO.input(btnPin)
        time.sleep(0.2)
        if btnState == False:
            print('Button Pressed')
            GPIO.output(ledPin, True)
        else:
            GPIO.output(ledPin, False)
except KeyboardInterrupt:
    GPIO.cleanup()

