
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

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

def spin(wheel, speed):
	if (speed > 0):
		wheel.run(Adafruit_MotorHAT.FORWARD)
		wheel.setSpeed(speed)
	elif (speed < 0):
		wheel.run(Adafruit_MotorHAT.BACKWARD)
		wheel.setSpeed(-speed)
	else:
		wheel.run(Adafruit_MotorHAT.RELEASE)

def spinMotor(motorId=1, speed=200, dur=-1):
	m = mh.getMotor(motorId)
	spin(m, speed)
	if (dur >= 0):
		time.sleep(dur)
		stop()
		
		
def stop():
	mFL.run(Adafruit_MotorHAT.RELEASE)
	mFR.run(Adafruit_MotorHAT.RELEASE)
	mBL.run(Adafruit_MotorHAT.RELEASE)
	mBR.run(Adafruit_MotorHAT.RELEASE)


def forward(speed=200, dur=-1):
	spin(mFR, speed)
	spin(mFL, speed)
	spin(mBR, speed)
	spin(mBL, speed)

	if (dur >= 0):
		time.sleep(dur)
		stop()
	
        
def backward(speed, dur=-1):
	spin(mFR, -speed)
	spin(mFL, -speed)
	spin(mBR, -speed)
	spin(mBL, -speed)

	if (dur >- 0):
		time.sleep(dur)
		stop()

        
def left(speed, dur=-1):
	spin(mFR, -speed)
	spin(mFL, speed)
	spin(mBR, -speed)
	spin(mBL, speed)

	if (dur >- 0):
		time.sleep(dur)
		stop()

def right(speed, dur=-1):
	spin(mFR, speed)
	spin(mFL, -speed)
	spin(mBR, speed)
	spin(mBL, -speed)

	if (dur >- 0):
		time.sleep(dur)
		stop()
        


