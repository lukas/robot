import RPi.GPIO as GPIO
import os
import time
import atexit

def setup():
    for i in range(3):
        GPIO.setup(TRIG[i],GPIO.OUT)
        GPIO.setup(ECHO[i],GPIO.IN)
        GPIO.output(TRIG[i], False)

        print "Waiting For Sensor To Settle"

if (os.environ['LTRIG']):
	TRIG = [int(os.environ['LTRIG']),
			int(os.environ['CTRIG']),
			int(os.environ['RTRIG'])]
	ECHO = [int(os.environ['LECHO']),
			int(os.environ['CECHO']),
			int(os.environ['RECHO'])]

	GPIO.setmode(GPIO.BCM)
	setup()

def turnOffGPIO():
	GPIO.cleanup()

atexit.register(turnOffGPIO)
		



def distance(i):
#    print "Distance Measurement In Progress"

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

 #   print "Distance:",distance,"cm"

    return distance

def ldist():
	return distance(0)

def rdist():
	return distance(2)

def cdist():
	return distance(1)
