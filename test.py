# Edukit 3 test
# (for Python3)

#imports
import RPi.GPIO as GPIO
import time

# ################
# Debug

def debug(text):
	print(text)

# init GPIO
debug("Init GPIO")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set GPIO pin modes
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

# Motors off
debug("Motors off")
GPIO.output(7, 0)
GPIO.output(8, 0)
GPIO.output(9, 0)
GPIO.output(10, 0)

# Right forwards
debug("right forwards")
GPIO.output(9, 0)
GPIO.output(10, 1)

# Left forwards
debug("right forwards")
GPIO.output(7, 1)
GPIO.output(8, 0)

# wait ...
debug("wait ...")
time.sleep(1)

# Stop
debug("Cleanup")
GPIO.cleanup()
