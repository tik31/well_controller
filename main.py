import machine
import time
import pump

def main():
	print('Firmware is running!')

	pump1 = pump.Pump(12, 14)
	pump2 = pump.Pump(26, 27)

	for x in range(1,5):
		pump1.on()
		time.sleep(3)
		pump1.off()

		time.sleep(5)

		pump2.on()
		time.sleep(3)
		pump2.off()

		time.sleep(5)