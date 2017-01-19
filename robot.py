#! /usr/bin/python

import wheels
import sys
import sonar

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
	wheels.forward(200, 1)

elif (cmd == 'backward'):
	wheels.backward(200, 1)

elif (cmd == 'left'):
	wheels.left(200, 1)

elif (cmd == 'right'):
	wheels.right(200, 1)

elif (cmd == 'wheel1'):
	wheels.spinMotor(1, 200, 1)

elif (cmd == 'wheel2'):
	wheels.spinMotor(2, 200, 1)

elif (cmd == 'wheel3'):
	wheels.spinMotor(3, 200, 1)

elif (cmd == 'wheel4'):
	wheels.spinMotor(4, 200, 1)

elif (cmd == 'shake'):
	wheels.left(200, 0.2)
	wheels.right(200, 0.2)

elif (cmd == 'leftdist'):
	print sonar.ldist()
elif (cmd == 'rightdist'):
	print sonar.rdist()
elif (cmd == 'centerdist'):
	print sonar.cdist()

else:
	print usage



	
