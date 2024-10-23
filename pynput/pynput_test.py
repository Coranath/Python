from pynput import keyboard

def pressed(key):
    print(f'{key} was pressed')
    if key == keyboard.Key.esc:
        return False

def release(key):
    print(f'{key} was released')

l = keyboard.Listener(on_press=pressed, on_release=release)

l.start()
l.join()

