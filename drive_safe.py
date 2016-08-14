
import subprocess

def do(cmd):
    print(cmd)
    p =subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

from random import random
    
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

from flask import Flask, render_template, request, Response, send_file

from camera_pi import Camera

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

TRIG = [23, 5, 22]
ECHO = [24, 6, 27]


def setup():
    for i in range(0,2):
        GPIO.setup(TRIG[i],GPIO.OUT)
        GPIO.setup(ECHO[i],GPIO.IN)
        GPIO.output(TRIG[i], False)

        print "Waiting For Sensor To Settle"
        

def distance(i):
    print "Distance Measurement In Progress"

    GPIO.output(TRIG[i], True)

    time.sleep(0.00001)

    GPIO.output(TRIG[i], False)

    pulse_end = 0;
    pulse_start = 0;
    
    while GPIO.input(ECHO[i])==0:
        pulse_start = time.time()

    while GPIO.input(ECHO[i])==1:
        pulse_end = time.time()
        
    if (pulse_end == 0 or pulse_start==0):
        return 1000
        
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print "Distance:",distance,"cm"

    return distance

    


import os
import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
        GPIO.cleanup()
        
atexit.register(turnOffMotors)

################################# DC motor test!
mFL = mh.getMotor(1)
mBL = mh.getMotor(2)
mBR = mh.getMotor(3)
mFR = mh.getMotor(4)

def wakeup(m):
        # set the speed to start, from 0 (off) to 255 (max speed)
        m.setSpeed(150)
        m.run(Adafruit_MotorHAT.FORWARD);
        # turn on motor
        m.run(Adafruit_MotorHAT.RELEASE);        


wakeup(mFL)
wakeup(mBL)
wakeup(mFR)
wakeup(mBL)
setup()

def gof():
        mBR.run(Adafruit_MotorHAT.BACKWARD)
        mBL.run(Adafruit_MotorHAT.BACKWARD)
        mFL.run(Adafruit_MotorHAT.BACKWARD)
        mFR.run(Adafruit_MotorHAT.BACKWARD)
        mBR.setSpeed(200)
        mBL.setSpeed(200)
        mFR.setSpeed(200)
        mFL.setSpeed(200)

def stop():
        mFL.run(Adafruit_MotorHAT.RELEASE)
        mFR.run(Adafruit_MotorHAT.RELEASE)
        mBL.run(Adafruit_MotorHAT.RELEASE)
        mBR.run(Adafruit_MotorHAT.RELEASE)

def left(speed, dur):
        print "Left "
        mFR.run(Adafruit_MotorHAT.BACKWARD)
        mFR.setSpeed(speed)

        time.sleep(dur)
        mFR.run(Adafruit_MotorHAT.RELEASE)
        return ''

def right(speed, dur):
        print "Right "
        mFL.run(Adafruit_MotorHAT.BACKWARD)
        mFL.setSpeed(speed)
        
        time.sleep(dur)
        mFL.run(Adafruit_MotorHAT.RELEASE)
        return ''


stopped = True;
turning = False;
THRESH = 25;

while(1==1):        
    d= distance();
    print(d);

    if (d>=THRESH and stopped==True):
        stopped=False;
        turning = False;
        gof();

    elif (d<THRESH and stopped==False):
        stopped=True;
    elif (d<THRESH and stopped==True):
        print ("Stopping");
        if (turning=False):
            do('echo "oh no" | festival --tts')
            
        stop();
        turning=True

        left(100, 0.7);

        time.sleep(0.3);
        stopped=True
