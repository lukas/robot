#! /usr/bin/python

import drive
import sys

usage = '''
robot

Tell the robot what to do.

Commands 

forward
backward
left
right
stop
wheel1
wheel2
wheel3
wheel4
shake
'''

print sys.argv

if (len(sys.argv) == 1):
	print usage
	exit

cmd = sys.argv[1]
	
if (cmd == 'forward'):
	drive.forward(200, 1)

elif (cmd == 'backward'):
	drive.backward(200, 1)

elif (cmd == 'left'):
	drive.left(200, 1)

elif (cmd == 'right'):
	drive.right(200, 1)

elif (cmd == 'wheel1'):
	drive.spinMotor(1, 200, 1)

elif (cmd == 'wheel2'):
	drive.spinMotor(2, 200, 1)

elif (cmd == 'wheel3'):
	drive.spinMotor(3, 200, 1)

elif (cmd == 'wheel4'):
	drive.spinMotor(4, 200, 1)

elif (cmd == 'shake'):
	drive.left(200, 0.25)
	drive.right(200, 0.25)

else:
	print usage



	
