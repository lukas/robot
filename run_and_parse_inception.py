import sys

import subprocess

imageFile = sys.argv[1]
dataFile = sys.argv[2]



def do(cmd):
	print(cmd)
	p =subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():
		print line

	retval = p.wait()

do('( cd /home/pi/tensorflow && ./label_image --image=../robot/'+imageFile+' > ../robot/raw.output )' )

do('tail -5 ../robot/raw.output | tail -5 ../tensorflow/t | cut -d"]" -f2 | cut -d"(" -f1 > ' + dataFile)
