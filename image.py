

import subprocess

def do(cmd):
	print(cmd)
	p =subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():
		print line

	retval = p.wait()


def classify(n):
	suffix = str(n)
	imageFile = 'images/img'+suffix+'.jpg'
	dataFile = 'images/data'+suffix
	latestImage = 'images/latest_img.jpg'
	latestData = 'images/latest_data'
        do('echo "I\'m thinking." | flite')
	do('cp /dev/shm/mjpeg/cam.jpg '+imageFile);
	do('ln -f '+imageFile+' '+latestImage);
	do('python run_and_parse_inception.py '+imageFile+ " " +dataFile)

	do('ln -f '+dataFile+' '+latestData);

        do('{ echo "I think I see a "; cat '+dataFile+' |  sed -e \'$ ! s/$/. or maybe a/\'; } | flite')

	do('echo '+suffix+' > images/INDEX')


i=0
read_data = 0

with open('images/INDEX', 'r') as f:
	read_data = int(f.read())

i += read_data + 1;


classify(i)
