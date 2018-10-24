def setup(robot_config):
from gpiozero import LED
from time import sleep
led = LED(17)
    return

def move(args):
    command = args['command']
    
    if command == 'L':
      led.on()
        return
    elif command == 'R':
       led.off()
        return
   return
