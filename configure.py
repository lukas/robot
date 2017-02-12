import json
import os.path

data={}

# Default configuration
# If you want to change make a json file that looks like
# {
#   "LTRIG":"17",
#   "CTRIG":"23",
#   "RTRIG":"22",
#   "LECHO":"18",
#   "CECHO":"24",
#   "RECHO":"27"
# }

data["LTRIG"] = 23 # default pin for left sonar trigger
data["CTRIG"] = 17 # default pin for center sonar trigger
data["RTRIG"] = 22 # default pin for right sonar trigger
data["LECHO"] = 24 # default pin for left sonar echo
data["CECHO"] = 18 # default pin for center sonar echo
data["RECHO"] = 27 # default pin for right sonar echo

if os.path.isfile('robot.conf'):
	with open('robot.conf') as data_file:
		data = json.load(data_file)
else:
	print("Couldn't find robot.conf file, using default configuration")
