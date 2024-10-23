from gpiozero import LED
from time import sleep

pin = input('Please enter the GPIO pin to use: ')

led = LED(pin)

val = ''

while(val.lower() != 'q'):

    val = input('Press enter to cycle the LED on and off, press q then enter to power off and quit...')
    
    if val.lower() == 'q':
        led.off()
    else:
        led.toggle()

print('All done, thanks!')