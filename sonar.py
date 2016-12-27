import RPi.GPIO as GPIO
import sys
import time
import atexit

#check a sonar with trigger argv1 and echo argv2
#example usage
#python sonar.py 22 27

# recommended for auto-disabling motors on shutdown!
def turnOffGPIO():
	GPIO.cleanup()	

atexit.register(turnOffGPIO)

GPIO.setmode(GPIO.BCM)

TRIG = int(sys.argv[1])

ECHO = int(sys.argv[2])

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)

print "Waiting For Sensor To Settle"

time.sleep(2)

GPIO.output(TRIG, True)

time.sleep(0.00001)

GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
    pulse_start = time.time()

while GPIO.input(ECHO)==1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print "Distance:",distance,"cm"


            
