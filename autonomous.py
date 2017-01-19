
import wheels
import sonar
import time





FORWARD=1
LEFT=2
RIGHT=3
BACKWARD=4

def autodrive(dur):
	start_time = time.time()
	end_time = time.time() + dur

	mode = FORWARD

	wheels.forward(-100)

	
	while(time.time() < end_time):
		time.sleep(0.1)
		cdist = sonar.cdist()
		ldist = sonar.ldist()
		rdist= sonar.rdist()

		print ("%d %d %d" % (ldist, cdist, rdist))
		
		if (mode == FORWARD):
			if (cdist < 25 or ldist <4 or rdist < 4):
				wheels.stop()
				if (ldist < rdist):
					mode=RIGHT
					wheels.right(-100)
				else:
					mode=LEFT
					wheels.left(-100)
				
		if (mode==LEFT or mode==RIGHT):
			if (cdist > 50):
				mode=FORWARD
				wheels.forawrd(-100)
				
			
			
	wheels.stop()


	
if (__name__ == '__main__'):
	autodrive(10)
