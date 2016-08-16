import sys

import subprocess

imageFile = sys.argv[1]
dataFile = sys.argv[2]



def do(cmd):
	print(cmd)
	p =subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	for line in p.stdout.readlines():
		print line

	retval = p.wait()

do('( cd /home/pi/tensorflow && ./label_image --image=../robot/'+imageFile+' ) &> ../robot/raw.output ' )

do('tail -5 raw.output | cut -d"]" -f2 | cut -d"(" -f1 > ' + dataFile)
