#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

from flask import Flask, render_template, request, Response, send_file

from camera_pi import Camera

app = Flask(__name__)



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




def gof():
        mBR.run(Adafruit_MotorHAT.FORWARD)
        mBL.run(Adafruit_MotorHAT.FORWARD)
        mFL.run(Adafruit_MotorHAT.FORWARD)
        mFR.run(Adafruit_MotorHAT.FORWARD)
        mBR.setSpeed(200)
        mBL.setSpeed(200)
        mFR.setSpeed(200)
        mFL.setSpeed(200)

def gob():
        mBR.run(Adafruit_MotorHAT.BACKWARD)
        mBL.run(Adafruit_MotorHAT.BACKWARD)
        mFR.run(Adafruit_MotorHAT.BACKWARD)
        mFL.run(Adafruit_MotorHAT.BACKWARD)
        mBR.setSpeed(200)
        mBL.setSpeed(200)
        mFR.setSpeed(200)
        mFL.setSpeed(200)

def gol():
        mBR.run(Adafruit_MotorHAT.BACKWARD)
        mBL.run(Adafruit_MotorHAT.FORWARD)
        mFR.run(Adafruit_MotorHAT.BACKWARD)
        mFL.run(Adafruit_MotorHAT.FORWARD)
        mBR.setSpeed(200)
        mBL.setSpeed(200)
        mFR.setSpeed(200)
        mFL.setSpeed(200)

def gor():
        mBR.run(Adafruit_MotorHAT.FORWARD)
        mBL.run(Adafruit_MotorHAT.BACKWARD)
        mFR.run(Adafruit_MotorHAT.FORWARD)
        mFL.run(Adafruit_MotorHAT.BACKWARD)
        mBR.setSpeed(200)
        mBL.setSpeed(200)
        mFR.setSpeed(200)
        mFL.setSpeed(200)

def stop():
        mFL.run(Adafruit_MotorHAT.RELEASE)
        mFR.run(Adafruit_MotorHAT.RELEASE)
        mBL.run(Adafruit_MotorHAT.RELEASE)
        mBR.run(Adafruit_MotorHAT.RELEASE)


        
def forward(speed, dur):
	print "Forward! "
	mR.run(Adafruit_MotorHAT.FORWARD)
	mL.run(Adafruit_MotorHAT.FORWARD)
	mR.setSpeed(speed)
	mL.setSpeed(speed)
	time.sleep(dur)
	
	mL.run(Adafruit_MotorHAT.RELEASE)
	mR.run(Adafruit_MotorHAT.RELEASE)
	return ''
        
def backward(speed, dur):
	print "Backward! "
	mR.run(Adafruit_MotorHAT.BACKWARD)
	mL.run(Adafruit_MotorHAT.BACKWARD)
	mR.setSpeed(speed)
	mL.setSpeed(speed)
	time.sleep(dur)
	
	mL.run(Adafruit_MotorHAT.RELEASE)
	mR.run(Adafruit_MotorHAT.RELEASE)
	return ''
        
def left(speed, dur):
	print "Left "
	mR.run(Adafruit_MotorHAT.BACKWARD)
	mR.setSpeed(speed)
	
	time.sleep(dur)
	mR.run(Adafruit_MotorHAT.RELEASE)
	return ''

def right(speed, dur):
	print "Right "
	mL.run(Adafruit_MotorHAT.BACKWARD)
	mL.setSpeed(speed)
	
	time.sleep(dur)
	mL.run(Adafruit_MotorHAT.RELEASE)
	return ''
        



#forward(200, 3)
#backward(200, 3)


@app.route("/")
def main():
        return render_template('index.html')

@app.route('/forward')
def fward():
        forward(200, 3)
        return ''

@app.route('/backward')
def bward():
        backward(200, 3)
        return ''

@app.route('/left')
def l():
        left(200, 3)
        return ''
        
@app.route('/forward')
def r():
        right(200, 3)
        return ''
        
@app.route('/f')
def gof_r():
        gof()
        return ''
        
@app.route('/b')
def gob_r():
        gob()
        return ''

@app.route('/r')
def gor_r():
        gor()
        return ''

@app.route('/l')
def gol_r():
        gol()
        return ''

@app.route('/stop')
def stop_r():
        stop()
        return ''

@app.route('/setSpeed')
def setSpeed():
	print 'gotParams';
	print request.query_string
	print request.args
	print request.args.getlist('name[]')
    #	print request.form.get('left',1,type=int)

    #print request.form.get('right',1,type=int)
	print request.args['right']
	print request.args['left']
	
	return ''

@app.route('/latest.jpg')
def latest():
	filename = 'images/latest_img.jpg'
	return send_file(filename, mimetype='image/jpg')

@app.route('/data')
def data():
	f = open('images/latest_data', 'r')
	data = f.read()
	return data

def gen(camera):
        """Video streaming generator function."""
        while True:
                frame = camera.get_frame()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                time.sleep(0.5)
                
@app.route('/video_feed')
def video_feed():
        """Video streaming route. Put this in the src attribute of an img tag."""
        return Response(gen(Camera()),
                        mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
        app.run()
