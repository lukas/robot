import subprocess

def say(text):
    subprocess.Popen(['flite', '-t',  text])


