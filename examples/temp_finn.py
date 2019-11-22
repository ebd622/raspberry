import time
from grove.factory import Factory

# connect to alalog pin 2(slot A2)
PIN = 0

sensor = Factory.getTemper("NTC-ADC", PIN)

sent=False
print('Detecting temperature...')
while True:
    t=sensor.temperature

    if t>26 and not sent:
      print('Too hot...')
      #TODO: push a notification
      sent=True

    if t<26 and sent:
      #Reset the flag
      sent=False
 


    print('{} Celsius'.format(t))
    time.sleep(1)

