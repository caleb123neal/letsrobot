from gpiozero import LED
from time import sleep
led = LED(17)

def setup(robot_config):
#haha nothing to set up! gotcha
    return

def move(args):
    command = args['command']
    
    if command == 'L down':
      led.on()
        return
    elif command == 'R down':
       led.off()
        return
   return
