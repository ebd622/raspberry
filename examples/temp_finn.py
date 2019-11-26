import time
import requests
from grove.factory import Factory

# connect to alalog pin 2(slot A2)
PIN = 0

sensor = Factory.getTemper("NTC-ADC", PIN)

sent=False
print('Detecting temperature...')
while True:
    t=sensor.temperature

    if t<24 and not sent:
      print('Too cold...')
      data = '{"actionID":"D0B7EB88-9098-4FDD-BA88-1B973154D2AF"}'
      url = "http://localhost:3001/actions"
      headers = {'content-type': 'application/json'}
      r = requests.post(url, data=data, headers=headers)

      #curl -d '{"actionID":"D0B7EB88-9098-4FDD-BA88-1B973154D2AF"}' -H "Content-Type: application/json" http://localhost:3001/actions
      #TODO: push a notification
      sent=True

    if t>24 and sent:
      #Reset the flag
      sent=False
 


    print('{} Celsius'.format(t))
    time.sleep(1)

