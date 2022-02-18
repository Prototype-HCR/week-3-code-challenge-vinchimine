import time
import neopixel
import board
import digitalio

# make a neopixel object for 10 pixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1)

# declare some inputs for button a and b
button_A = digitalio.DigitalInOut(board.BUTTON_A)
button_A.switch_to_input(pull=digitalio.Pull.DOWN)
button_B = digitalio.DigitalInOut(board.BUTTON_B)
button_B.switch_to_input(pull=digitalio.Pull.DOWN)

# declare some color constants
RED = (255, 0, 0)
ORANGE = (252, 70, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

colors = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]

color = RED

button_a_pre = button_A.value
button_b_pre = button_B.value

press_count = False
a_press_time = time.monotonic()
b_press_time = time.monotonic()

brightness_val = 0.5
brightness_inc = -0.1

pixel_mode = False
led_state = False

while True:
    # gather input values
    button_a_read = button_A.value
    button_b_read = button_B.value

    if button_a_read != button_a_pre:
        print("Button A Has Changed")
        if button_a_read:
            a_press_time = time.monotonic()
            # set a variable to True to show that the button was pushed

            print("Button A changed from Not to Press")
        else:
            # the button has changed from True to False
            print("Button A changed from Press to Not")
            # if the time since the button was pressed is LESS than 2...
            if time.monotonic() - a_press_time < 0.5:
                led_state = not led_state
    else:
        if button_a_read:
            print("Button A is Pressed")
            # decrese the brightness
            if time.monotonic() - a_press_time > 0.5:
                # it has been 1 second since the button has not changed
                # decrease the brightness value of the pixels
                brightness_val = brightness_val - 0.1
                print(brightness_val)
                # constrains the bightness_val to a limit
                if brightness_val <= 0:
                    brightness_val = 0.1
                # the button has been pressed for while set the varible that was set when the button was pressed to False

                pixels.brightness = brightness_val
                time.sleep(0.1)

    # check for change in the button state
    if button_b_read != button_b_pre:
        # the button has changed...
        print("Button B Has Changed")
        if button_b_read:
            # the button has changed from False to True
            b_press_time = time.monotonic()
            print("Button B changed from Not to Press")
        else:
            if time.monotonic() - b_press_time < 0.5:
               press_count += 1
               if press_count > 7:
                  press_count = 0
                  print(press_count)
            # the button has changed from True to False
            print("Button B changed from Press to Not")

    else:
        if button_b_read:
            print("Button B is Pressed")
            if time.monotonic() - b_press_time > 0.5:
                # it has been 1 second since the button has not changed
                # decrease the brightness value of the pixels
                brightness_val = brightness_val + 0.1
                print(brightness_val)
                # constrains the bightness_val to a limit
                if brightness_val >= 1:
                    brightness_val = 1.0
                # the button has been pressed for while set the varible that was set when the button was pressed to False

                pixels.brightness = brightness_val
                time.sleep(0.1)

    # do our output based on the input conditions
    if led_state:
        # if led state is true, fill the leds with the selected color
       pixels.fill(colors[press_count])
     # led on to off
    else:
        pixels.fill(OFF)

    # save the button_a_read value for next time
    button_a_pre = button_a_read
    button_b_pre = button_b_read
    time.sleep(0.1)
