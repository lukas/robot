import subprocess
import os

def say(text):
	if 'VOICE' in os.environ:
		voice = os.environ['VOICE']
		subprocess.Popen(['flite', '-voice', voice,'-t',  text])
	else:	
		subprocess.Popen(['flite', '-t',  text])


