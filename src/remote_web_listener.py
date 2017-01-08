#!/usr/bin/python

import time

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for

import RPi.GPIO as GPIO
from car_controller import CarController

# config items
timeInterval = 0.7

GPIO.setmode(GPIO.BCM)
carController = CarController()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/controlit', methods = ['POST'])
def control():
    buttonHit = request.form['buttonPress']
    print("The button hit is '" + buttonHit + "'")
    if buttonHit == 'Fast':
        print(buttonHit)
    elif buttonHit == 'Slow':
        print(buttonHit)
    elif buttonHit == 'Foward':
        carController.forward()
        time.sleep(timeInterval)
        carController.stop()
	print ("Move Foward")
    elif buttonHit == 'Back':
        carController.reverse()
        time.sleep(timeInterval)
        carController.stop()
	print ("Move Back")
    elif buttonHit == 'Left':
        carController.forwardLeft()
        time.sleep(timeInterval)
        carController.stop()
	print ("Move Left")
    elif buttonHit == 'Right':
        carController.forwardRight()
        time.sleep(timeInterval)
        carController.stop()
	print ("Move Right")
    else :
        print("Do Nothing")
    
    return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
