# robot

This will run a simple robot with a webserver on a raspberry PI with the Adafruit Motor Hat.  I wrote this up for myself for fun and to help me remember how I set things up.

This is all designed for a Raspberry PI 3 with the Adafruit Motor Hat for cars and the Adafruit Servo Hat for arms

# Programs

The robot.py program will run commands from the commandline
The drive_server.py runs a web server for driving around

# Wiring Wheels

You can easily change this but this is what wheels.py expects

M1 - Front Left
M2 - Back Left (optional)
M3 - Back Right (optional)
M4 - Front Right 


## Install


### nginx

copy the configuration file at nginx/nginx.conf to /etc/nginx/nginx.conf

### gunicorn

To setup the gunicorn webservice service modify

/etc/systemd/system/gunicorn.service

```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=pi
Group=www-data
WorkingDirectory=/home/pi/robot
ExecStart=/usr/local/bin/gunicorn --workers 3 --bind unix:/home/pi/drive.sock drive:app

[Install]
WantedBy=multi-user.target
```