#!/usr/bin/python
import RPi.GPIO as GPIO
import time

##Define a function named Blink()
def Blink(numTimes,duration):
    half_duration = duration/2
    for i in range(0,numTimes): 
        print "Blink " + str(i+1) 
        GPIO.output(7, True) 
        time.sleep(half_duration) 
        GPIO.output(7, False)  
        time.sleep(half_duration) 
    print "Done" 

#~### Start of Execution
GPIO.setmode(GPIO.BOARD)
# GPIO Pin connected to LED
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, True)
time.sleep(0.5)
GPIO.output(7, False)

## Ask user for total number of blinks and length of each blink
iterations = raw_input("Enter total number of times to blink: ")
duration = raw_input("Enter duration of each blink(seconds): ")

Blink(int(iterations),float(duration))

GPIO.cleanup()

