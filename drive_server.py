#!/usr/bin/python

from flask import Flask, render_template, request, Response, send_file
from camera_pi import Camera
import wheels
import speaker
import autonomous
import os

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route('/forward')
def forward():
	wheels.forward(200, 3)
	return ''

@app.route('/backward')
def backward():
	wheels.backward(200, 3)
	return ''


@app.route('/shake')
def shake():
	wheels.left(200, 0.2)
	wheels.right(200, 0.2)
        return ''

@app.route('/left')
def left():
	wheels.left(200, 3)
	return ''
        
@app.route('/right')
def right():
	wheels.right(200, 3)
	return ''
        
@app.route('/f')
def f():
	wheels.forward(200)
	return ''
        
@app.route('/b')
def b():
	wheels.backward(200)
	return ''

@app.route('/r')
def r():
	wheels.right(200)
	return ''

@app.route('/l')
def l():
	wheels.left(200)
	return ''

@app.route('/stop')
def stop():
	wheels.stop()
	return ''

@app.route('/latest.jpg')
def latest():
	filename = 'images/latest_img.jpg'
	return send_file(filename, mimetype='image/jpg')


@app.route('/drive')
def drive():
        time = 10
        if 'time' in request.args:
                time = request.args.get('time')
                

        autonomous.autodrive(time)

        return ''
        
@app.route('/say')
def say():
        text = request.args.get('text')
        speaker.say(text)
        return ''

@app.route('/data')
def data():
	img_num = request.args.get('i')
	if img_num is None:
		filename = 'images/latest_data'
	else:
		filename = 'images/data'+img_num
		
	f = open(filename, 'r')
	data = f.read()
	return data
   
@app.route('/img_rec')
def img_rec():
        wheels.stop()
#	os.system('python image.py')
        return ''

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
