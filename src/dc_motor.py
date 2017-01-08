#!/usr/bin/python
import RPi.GPIO as GPIO
import time


class SimpleMotorController(object):
    """Able to start motor
       TODO : consider how to inject the pins to allow
              to control multiple motors"""

    def __init__(self, enablePin, motorPinA, motorPinB):
        GPIO.setup(enablePin, GPIO.OUT)
        GPIO.setup(motorPinA, GPIO.OUT)
        GPIO.setup(motorPinB, GPIO.OUT)
        self.enablePin = enablePin
        self.motorPinA = motorPinA
        self.motorPinB = motorPinB

    def moveClockwise(self):
        """docstring for moveClockwise"""
        GPIO.output(self.motorPinA, GPIO.LOW)
        GPIO.output(self.motorPinB, GPIO.HIGH)
        GPIO.output(self.enablePin, GPIO.HIGH)

    def moveAntiClockwise(self):
        """docstring for moveAntiClockwise"""
        GPIO.output(self.motorPinA, GPIO.HIGH)
        GPIO.output(self.motorPinB, GPIO.LOW)
        GPIO.output(self.enablePin, GPIO.HIGH)


    def stop(self):
        """docstring for stop"""
        GPIO.output(self.motorPinA, GPIO.LOW)
        GPIO.output(self.motorPinB, GPIO.LOW)
        GPIO.output(self.enablePin, GPIO.LOW)
            
       
def main():
    """docstring for main"""
    # uses the Broadcom pins as on the silkscreen of the breakout board
    GPIO.setmode(GPIO.BCM) 

    directionEnablePin = 14  # connector pin 8
    directionPinA =  15  # connector pin 10
    directionPinB = 18  # connector pin 12

    acceleratorEnablePin = 17  # connector pin 11
    acceleratorPinA =  27  # connector pin 13
    acceleratorPinB = 22  # connector pin 15

    
    directionMotor = SimpleMotorController(directionEnablePin, 
                                           directionPinA,
                                           directionPinB) 

    acceleratorMotor = SimpleMotorController(acceleratorEnablePin, 
                                             acceleratorPinA,
                                             acceleratorPinB) 

    directionMotor.moveClockwise() # moves right
    time.sleep(1)
    directionMotor.stop()
    time.sleep(1)
    directionMotor.moveAntiClockwise() # moves left
    time.sleep(1)
    directionMotor.stop()


    acceleratorMotor.moveClockwise() # moves  forward
    time.sleep(1)
    acceleratorMotor.stop()
    time.sleep(1)
    acceleratorMotor.moveAntiClockwise() # reverses
    time.sleep(1)
    acceleratorMotor.stop()

    GPIO.cleanup()

#~### Start of Execution

if __name__ == '__main__':
    main()




