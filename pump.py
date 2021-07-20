from machine import Pin
import time

class Pump():
	"""docstring for Pump"""

	
	def __init__(self, _pin1, _pin2):
		self.pin1 = Pin(_pin1, Pin.OUT)
		self.pin2 = Pin(_pin2, Pin.OUT)

        
	def on(self):
		self.pin1.on()
		time.sleep(1)
		self.pin2.on()


	def off(self):
		self.pin1.off()
		self.pin2.off()
