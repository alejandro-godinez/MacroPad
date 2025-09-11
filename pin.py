"""
Functionality for handling the MacroPad PIN code lock.
"""

import time
import displayio
import terminalio
import random
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label

# A 6-digit PIN code to unlock the device.
PIN_CODE = "123456"

def check_pin(macropad):
    """
    Displays a keypad on the MacroPad screen and waits for the correct PIN to be entered.
    """

    # Create a display group for the PIN entry screen
    pin_group = displayio.Group()

    # Title label
    pin_title_label = label.Label(
        terminalio.FONT,
        text="Enter PIN:",
        color=0xFFFFFF,
        anchored_position=(10, 5), # Left-align the title
        anchor_point=(0.0, 0.0)
    )
    pin_group.append(pin_title_label)

    # PIN code entry label
    pin_text_label = label.Label(
        terminalio.FONT,
        text="",
        color=0xFFFFFF,
        anchored_position=(10 + pin_title_label.bounding_box[2] + 5, 5), # Position the text to the right of the title
        anchor_point=(0.0, 0.0)
    )
    pin_group.append(pin_text_label)

    # Keypad layout labels
    keypad_labels = displayio.Group()
    keypad_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    # Initialize the labels once
    for i in range(12):
        key_label = label.Label(
            terminalio.FONT,
            text='',
            color=0xFFFFFF,
            anchored_position=(0, 0),
            anchor_point=(0.5, 1.0)
        )
        keypad_labels.append(key_label)
    pin_group.append(keypad_labels)

    # Helper function to shuffle and update the keypad labels
    def render_keypad():
        # Map the 12 keys to a numeric pad layout
        # Row 1: 1, 2, 3
        # Row 2: 4, 5, 6
        # Row 3: 7, 8, 9
        # Row 4: Cancel, 0, Enter

        # Numbers to be shuffled
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        # Manual shuffling of the numbers
        for i in range(len(numbers) - 1, 0, -1):
            j = random.randint(0, i)
            numbers[i], numbers[j] = numbers[j], numbers[i]

        # Create a new key mapping with shuffled numbers, keeping C and E fixed
        KEY_MAPPING = {}
        for i in range(12):
            if i in (9, 11): # fixed positions for Cancel and Enter
                KEY_MAPPING[i] = 'C' if i == 9 else 'E'
            else:
                KEY_MAPPING[i] = numbers.pop(0)

        # Update the display labels with the new mapping
        for i, key_index in enumerate(keypad_positions):
            x = i % 3
            y = i // 3
            keypad_labels[i].text = KEY_MAPPING[key_index]
            keypad_labels[i].anchored_position = (
                macropad.display.width * (x + 1) / 4,
                macropad.display.height * 0.45 + (y * macropad.display.height * 0.15)
            )

        return KEY_MAPPING

    # Initial render of the keypad
    current_key_mapping = render_keypad()

    # Set the root group to the PIN group and refresh the display
    macropad.display.root_group = pin_group
    macropad.display.refresh()

    entered_pin = ""
    pin_correct = False

    while not pin_correct:
        event = macropad.keys.events.get()
        if event and event.pressed:
            if event.key_number in current_key_mapping:
                macropad.pixels[event.key_number] = 0xFFFFFF
                macropad.pixels.show()
                time.sleep(0.1)

                key_value = current_key_mapping[event.key_number]

                if key_value.isdigit() and len(entered_pin) <= 6:
                    print("Key: ", key_value)
                    entered_pin += key_value
                    pin_text_label.text = "*" * len(entered_pin)
                elif key_value == 'C':
                    entered_pin = ""
                    pin_text_label.text = ""
                elif key_value == 'E':
                    if entered_pin == PIN_CODE:
                        pin_correct = True
                        for i in range(12):
                            macropad.pixels[i] = 0x00FF00
                        macropad.pixels.show()
                        time.sleep(1)
                    else:
                        pin_text_label.text = "INCORRECT"
                        for i in range(12):
                            macropad.pixels[i] = 0xFF0000
                        macropad.pixels.show()
                        time.sleep(1)
                        macropad.pixels.fill(0)
                        macropad.pixels.show()
                        entered_pin = ""
                        pin_text_label.text = ""

            macropad.pixels[event.key_number] = 0
            macropad.pixels.show()

            # Re-render the keypad with new shuffled keys after each press
            current_key_mapping = render_keypad()
            macropad.display.refresh()
