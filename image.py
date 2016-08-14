

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
	do('cp /dev/shm/mjpeg/cam.jpg '+imageFile);
	do('python classify_image.py --image_file '+imageFile+' > '+dataFile)
	do('ln -f '+imageFile+' '+latestImage);
	do('ln -f '+dataFile+' '+latestData);
        do('cut -d\'(\' -f1 '+dataFile+' | festival --tts');

i=0
while i<1:
	i=i+1
	classify(i%10)
