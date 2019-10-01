from gpiozero import LED
from gpiozero import MotionSensor

pir = MotionSensor(5)
led=LED(16)

while True:
	pir.wait_for_motion()
	print("You moved")
	led.on()
	pir.wait_for_no_motion()
	led.off()

