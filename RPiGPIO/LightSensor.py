from gpiozero import LightSensor

pin = input('Please enter the GPIO pin to use: ')

ldr = LightSensor(pin)

print("I'm gonna wait for light")
ldr.wait_for_light()
print('It worked eh?')