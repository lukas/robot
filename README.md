# robot

This will run a simple robot with a webserver on a raspberry PI with the Adafruit Motor Hat.  I wrote this up for myself for fun and to help me remember how I set things up.

This is all designed for a Raspberry PI 3 with the Adafruit Motor Hat for cars and the Adafruit Servo Hat for arms

## Programs

robot.py program will run commands from the commandline
sonar.py tests sonar wired into GPIO ports 
drive_server.py runs a web server for driving around
drive_safe.py runs a simple object avoidance algorithm

## Wiring The Robot
### Sonar

If you want to use the default sonar configuation

Left sonar trigger GPIO port 23 echo 24
Center sonar trigger GPIO port 17 echo 18
Right sonar trigger GPIO port 22 echo 27

### Wheels

You can easily change this but this is what wheels.py expects

M1 - Front Left
M2 - Back Left (optional)
M3 - Back Right (optional)
M4 - Front Right 


## Installation

### basic setup

There are a ton of articles on how to do basic setup of a Raspberry PI - one good one is here https://www.howtoforge.com/tutorial/howto-install-raspbian-on-raspberry-pi/

You will need to turn on i2c and optionall the camera

```
raspi-config
```

Next you will need to download i2c tools and smbus

```
sudo apt-get install i2c-tools python-smbus python3-smbus
```

Test that your hat is attached and visible with

```
sudo i2cdetect -y 1
```

Install dependencies

```
pip install -r requirements.txt
```

At this point you should be able to drive your robot locally, try:

```
./robot.py forward
```

### server

To run a webserver in the background with a camera you need to setup gunicorn and nginx

#### nginx

Nginx is a lightway fast reverse proxy - we store the camera image in RAM and serve it up directly.  This was the only way I was able to get any kind of decent fps from the raspberry pi camera.  We also need to proxy to gunicorn so that the user can control the robot from a webpage.

copy the configuration file from nginx/nginx.conf to /etc/nginx/nginx.conf

```
sudo cp nginx/nginx.conf /etc/nginx/nginx.conf
```

#### gunicorn

copy configuration file from gunicorn/gunicorn.service /etc/systemd/system/gunicorn.service

```
sudo cp gunicorn/gunicorn.service /etc/systemd/system/gunicorn.service
```

start the gunicorn service


```
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
```