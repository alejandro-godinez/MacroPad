"""
Functionality for handling the MacroPad PIN code lock.
"""

import time
import displayio
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label

# A 6-digit PIN code to unlock the device.
PIN_CODE = "123456"

def check_pin(macropad):
    """
    Displays a keypad on the MacroPad screen and waits for the correct PIN to be entered.
    """
    # Map the 12 keys to a numeric pad layout
    # Row 1: 1, 2, 3
    # Row 2: 4, 5, 6
    # Row 3: 7, 8, 9
    # Row 4: Cancel, 0, Enter
    KEY_MAPPING = {
        0: '1', 1: '2', 2: '3',
        3: '4', 4: '5', 5: '6',
        6: '7', 7: '8', 8: '9',
        9: 'C', 10: '0', 11: 'E'
    }

    # Create a display group for the PIN entry screen
    pin_group = displayio.Group()

    # Title label
    pin_title_label = label.Label(
        terminalio.FONT,
        text="Enter PIN:",
        color=0xFFFFFF,
        anchored_position=(macropad.display.width // 2, 5),
        anchor_point=(0.5, 0.0)
    )
    pin_group.append(pin_title_label)

    # PIN code entry label
    pin_text_label = label.Label(
        terminalio.FONT,
        text="",
        color=0xFFFFFF,
        anchored_position=(macropad.display.width // 2, 25),
        anchor_point=(0.5, 0.0)
    )
    pin_group.append(pin_text_label)

    # Keypad layout labels
    keypad_labels = displayio.Group()
    keypad_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for i, key_index in enumerate(keypad_positions):
        x = i % 3
        y = i // 3
        key_label = label.Label(
            terminalio.FONT,
            text=KEY_MAPPING[key_index],
            color=0xFFFFFF,
            anchored_position=(
                macropad.display.width * (x + 1) / 4,
                macropad.display.height * 0.45 + (y * macropad.display.height * 0.15)
            ),
            anchor_point=(0.5, 1.0)
        )
        keypad_labels.append(key_label)
    pin_group.append(keypad_labels)

    # Set the root group to the PIN group and refresh the display
    macropad.display.root_group = pin_group
    macropad.display.refresh()

    entered_pin = ""
    pin_correct = False
    while not pin_correct:
        event = macropad.keys.events.get()
        if event and event.pressed:
            if event.key_number in KEY_MAPPING:
                macropad.pixels[event.key_number] = 0xFFFFFF
                macropad.pixels.show()
                time.sleep(0.1)

                key_value = KEY_MAPPING[event.key_number]

                if key_value.isdigit() and len(entered_pin) < 6:
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
