# robot

This will run a simple robot with a webserver on a raspberry PI with the Adafruit Motor Hat.  I wrote this up for myself for fun and to help me remember how I set things up.

High level overview can be found in this article: https://www.oreilly.com/learning/how-to-build-a-robot-that-sees-with-100-and-tensorflow

## Hardware

- Raspberry PI 3
- 16GB (or larger) SIM Card
- Adafruit Motor Hat (for wheels)
- Any chassis with DC motors - for example: https://www.amazon.com/Emgreat-Chassis-Encoder-wheels-Battery/dp/B00GLO5SMY/ref=sr_1_2?ie=UTF8&qid=1486959207&sr=8-2&keywords=robot+chassis
- Adafruit Servo Hat (for arms)
- HC-SR04 sonars
- Any stepper motor arm - for example: SainSmart DIY Control Palletizing Robot Arm for the arm (https://www.amazon.com/dp/B0179BTLZ2/ref=twister_B00YTW763Y?_encoding=UTF8&psc=1)
- Raspberry PI compatible camera - for example: https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS/ref=sr_1_1?s=electronics&ie=UTF8&qid=1486960149&sr=1-1&keywords=raspberry+pi+camera

To get started, you should be able to make the robot work without the arm, sonar and servo hat.

## Programs

- robot.py program will run commands from the commandline
- sonar.py tests sonar wired into GPIO ports
- wheels.py tests simple DC motor wheels
- arm.py tests a servo controlled robot arm
- autonomous.py implements a simple driving algorithm using the wheels and sonal
- inception_server.py runs an image classifying microservice

## Example Robots

Here are two robots I made that use this software

![Robots](https://joyfulgrit.files.wordpress.com/2013/10/img_0183.jpg?w=700)

## Wiring The Robot
### Sonar

If you want to use the default sonar configuation, wire like this:

- Left sonar trigger GPIO pin 23 echo 24
- Center sonar trigger GPIO pin 17 echo 18
- Right sonar trigger GPIO pin 22 echo 27

You can modify the pins by making a robot.conf file.

### Wheels

You can easily change this but this is what wheels.py expects

- M1 - Front Left
- M2 - Back Left (optional - leave unwired for 2wd chassis)
- M3 - Back Right (optional - leave unwired for 2wd chassis)
- M4 - Front Right 


## Installation

### basic setup

There are a ton of articles on how to do basic setup of a Raspberry PI - one good one is here https://www.howtoforge.com/tutorial/howto-install-raspbian-on-raspberry-pi/

You will need to turn on i2c and optionally the camera

```
raspi-config
```

Next you will need to download i2c tools and smbus

```
sudo apt-get install i2c-tools python-smbus python3-smbus
```

Test that your hat is attached and visible with

```
i2cdetect -y 1
```

Install this code

```
sudo apt-get install git
git clone https://github.com/lukas/robot.git
cd robot
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
sudo apt-get install nginx
sudo cp nginx/nginx.conf /etc/nginx/nginx.conf
```

restart nginx

```
sudo nginx -s reload
```

#### gunicorn

install gunicorn


copy configuration file from services/web.service /etc/systemd/system/web.service

```
sudo cp services/web.service /etc/systemd/system/web.service
```

start gunicorn web app service

```
sudo systemctl daemon-reload
sudo systemctl enable web
sudo systemctl start web
```

Your webservice should be started now.  You can try driving your robot with buttons or arrow keys

#### camera

In order to stream from the camera you can use RPi-cam.  It's documented at http://elinux.org/RPi-Cam-Web-Interface but you can also just run the following

```
git clone https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git
cd RPi_Cam_Web_Interface
chmod u+x *.sh
./install.sh
```

Now a stream of images from the camera should be constantly updating the file at /dev/shm/mjpeg.  Nginx will serve up the image directly if you request localhost/cam.jpg.

#### tensorflow

There is a great project at https://github.com/samjabrahams/tensorflow-on-raspberry-pi that gives instructions on installing tensorflow on the Raspberry PI.  Recently it's gotten much easier, just do

```
wget https://github.com/samjabrahams/tensorflow-on-raspberry-pi/releases/download/v0.11.0/tensorflow-0.11.0-cp27-none-linux_armv7l.whl
sudo pip install tensorflow-0.11.0-cp27-none-linux_armv7l.whl
```

Next start a tensorflow service that loads up an inception model and does object recognition the the inception model

```
sudo cp services/inception.service /etc/systemd/system/inception.service
sudo systemctl daemon-reload
sudo systemctl enable inception
sudo systemctl start inception
```





