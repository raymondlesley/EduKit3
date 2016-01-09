# EduKit3brary for CamJam EduKit #3 - Robitics

#imports
import RPi.GPIO as GPIO

class Robot: 
	__DEBUG = False

	# #################################
	# __init__
	#
	def __init__(self, DEBUG=False):
		self.__DEBUG = DEBUG
		self._debug("Init")
		# init GPIO
		self._debug("Init GPIO")
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)

		# set GPIO pin modes
		GPIO.setup(7, GPIO.OUT)
		GPIO.setup(8, GPIO.OUT)
		GPIO.setup(9, GPIO.OUT)
		GPIO.setup(10, GPIO.OUT)

		# Motors off
		self._debug("Motors off")
		GPIO.output(7, 0)
		GPIO.output(8, 0)
		GPIO.output(9, 0)
		GPIO.output(10, 0)

	# #################################
	# _debug
	#
	def _debug(self, text):
		if (self.__DEBUG): print("EduKit3: " + text)


	# #################################
	# _right_stop
	# Right wheel stop
	#
	def _right_stop(self):
		self._debug("right stop")
		GPIO.output(9, 0)
		GPIO.output(10, 0)

	# #################################
	# _right_fwd
	# Right wheel forwards
	#
	def _right_fwd(self):
		self._debug("right forwards")
		GPIO.output(9, 0)
		GPIO.output(10, 1)

	# #################################
	# _right_back
	# Right wheel backwards
	#
	def _right_back(self):
		self._debug("right backwards")
		GPIO.output(9, 1)
		GPIO.output(10, 0)

	# #################################
	# _left_stop
	# Left forwards
	#
	def _left_stop(self):
		self._debug("left stop")
		GPIO.output(7, 0)
		GPIO.output(8, 0)

	# #################################
	# _left_fwd
	# Left forwards
	#
	def _left_fwd(self):
		self._debug("left forwards")
		GPIO.output(7, 1)
		GPIO.output(8, 0)

	# #################################
	# _left_back
	# Left backwards
	#
	def _left_back(self):
		self._debug("left backwards")
		GPIO.output(7, 0)
		GPIO.output(8, 1)

	# #################################
	# Stop
	# stop motors
	#
	def Stop(self):
		self._right_stop()
		self._left_stop()

	# #################################
	# Forwards
	# move forwards
	#
	def Forwards(self):
		self._right_fwd()
		self._left_fwd()
