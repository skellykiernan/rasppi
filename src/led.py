#!/usr/bin/python
import RPi.GPIO as GPIO
import time

##Define a function named Blink()
def Blink(numTimes,speed):
    for i in range(0,numTimes): 
        print "Blink " + str(i+1) 
        GPIO.output(7, True) 
        time.sleep(speed) 
        GPIO.output(7, False)  
        time.sleep(speed) 
    print "Done" 

#~### Start of Execution
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, True)
time.sleep(0.5)
GPIO.output(7, False)

## Ask user for total number of blinks and length of each blink
iterations = raw_input("Enter total number of times to blink: ")
speed = raw_input("Enter length of each blink(seconds): ")

Blink(int(iterations),float(speed))

GPIO.cleanup()

