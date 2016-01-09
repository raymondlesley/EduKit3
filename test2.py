# Edukit 3 test
# (for Python3)

#imports
from EduKit3Robot.Robot import Robot
import time

# ################
# Debug

DEBUG = True

def debug(text):
	if (DEBUG): print("test: " + text)

robot = Robot(DEBUG)

debug("Forwards")
robot.Forwards()

debug("wait ...")
time.sleep(1)

debug("... and stop")
robot.Stop()


