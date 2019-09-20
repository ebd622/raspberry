import time
from grove.gpio import GPIO

led = GPIO(16, GPIO.OUT)
button = GPIO(5, GPIO.IN)

while True:
    if button.read():
        led.write(1)
    else:
        led.write(0)
    time.sleep(0.1)
