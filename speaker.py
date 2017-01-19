import subprocess

def say(text):
	voice = os.environ['VOICE']:
	if voice:
		subprocess.Popen(['flite', '-voice', voice,'-t',  text])
	else:	
		subprocess.Popen(['flite', '-t',  text])


