import time
from grove.grove_led import GroveLed

# connect to pin 5(slot D5)
PIN   = 5
led = GroveLed(PIN)

while True:
   led.on()
   print("On")
   time.sleep(1)
   led.off()
   print("Off")
   time.sleep(1)
