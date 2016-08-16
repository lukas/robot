#! /bin/bash

( cd /home/pi/tensorflow && ./label_image --image=../robot/$1) &> ../robot/raw.output  
tail -5 raw.output | cut -d"]" -f2 | cut -d"(" -f1 > $2
