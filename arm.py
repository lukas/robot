#!/usr/bin/python


from flask import Flask, render_template, request, Response, send_file

import os
import atexit

from Adafruit_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

app = Flask(__name__)

def setServoPulse(channel, pulse):
        pulseLength = 1000000                   # 1,000,000 us per second
        pulseLength /= 60                       # 60 Hz
        print "%d us per period" % pulseLength
        pulseLength /= 4096                     # 12 bits of resolution
        print "%d us per bit" % pulseLength
        pulse *= 1000
        pulse /= pulseLength
        pwm.setPWM(channel, 0, pulse)


@app.route("/")
def main():
        return render_template('arm.html')

@app.route('/slider')
def slider():
        num = int(request.args.get('num'))
        value = int(request.args.get('value'))
        print("%i %i" % (num, value))
        fraction = int(servoMin + (value/100.0)*(servoMax - servoMin))
        print("Setting servo to %i" % fraction)
        pwm.setPWM(num, 0, fraction)
        return ""


if __name__ == "__main__":
        app.run()
