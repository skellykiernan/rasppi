#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from dc_motor import SimpleMotorController


class CarController(object):
    """docstring for CarController"""
    def __init__(self):
        super(CarController, self).__init__()
        directionEnablePin = 14  # connector pin 8
        directionPinA =  15  # connector pin 10
        directionPinB = 18  # connector pin 12

        acceleratorEnablePin = 17  # connector pin 11
        acceleratorPinA =  27  # connector pin 13
        acceleratorPinB = 22  # connector pin 15


        self.directionMotor = SimpleMotorController(directionEnablePin,
                                                    directionPinA,
                                                    directionPinB)

        self.acceleratorMotor = SimpleMotorController(acceleratorEnablePin,
                                                      acceleratorPinA,
                                                      acceleratorPinB)


    def forward(self):
        """docstring for forward"""
        self.acceleratorMotor.moveClockwise()

    def forwardLeft(self):
        """docstring for  forwardLeft"""
        self.directionMotor.moveAntiClockwise() # moves left 
        self.acceleratorMotor.moveClockwise()

    def forwardRight(self):
        """docstring for  forwardRight"""
        self.directionMotor.moveClockwise() # moves right
        self.acceleratorMotor.moveClockwise()

    def reverse(self):
        """docstring for reverse"""
        self.acceleratorMotor.moveAntiClockwise()

    def reverseLeft(self):
        """docstring for  reverseLeft"""
        self.directionMotor.moveClockwise() # moves left in reverse 
        self.acceleratorMotor.moveAntiClockwise()

    def reverseRight(self):
        """docstring for  reverseRight"""
        self.directionMotor.moveAntiClockwise() # moves right in reverse 
        self.acceleratorMotor.moveAntiClockwise() # will move reverse

    def stop(self):
        """docstring for stop"""
        self.directionMotor.stop()
        self.acceleratorMotor.stop()

def main():
    """docstring for main"""
    # uses the Broadcom pins as on the silkscreen of the breakout board
    GPIO.setmode(GPIO.BCM)
    carController = CarController()



## Move Forward
    carController.forward()
    time.sleep(1)
    carController.stop()
    time.sleep(0.5)
## More Forward Right
    carController.forwardRight()
    time.sleep(1)
    carController.stop()
    time.sleep(0.5)
## Move Forward Left
    carController.forwardLeft()
    time.sleep(1)
    carController.stop()
    time.sleep(0.5)
## Reverse
    carController.reverse()
    time.sleep(1)
    carController.stop()
    time.sleep(0.5)
## Reverse Left
    carController.reverseLeft()
    time.sleep(1)
    carController.stop()
    time.sleep(0.5)
## Reverse Right
    carController.reverseRight()
    time.sleep(1)
    carController.stop()


#    directionMotor.moveClockwise() # moves right
#    time.sleep(1)
#    directionMotor.stop()
#    time.sleep(1)
#    directionMotor.moveAntiClockwise() # moves left
#    time.sleep(1)
#    directionMotor.stop()


#    acceleratorMotor.moveClockwise() # moves  forward
#    time.sleep(1)
#    acceleratorMotor.stop()
#    time.sleep(1)
#    acceleratorMotor.moveAntiClockwise() # reverses
#    time.sleep(1)
#    acceleratorMotor.stop()

    GPIO.cleanup()

#~### Start of Execution

if __name__ == '__main__':
    main()
