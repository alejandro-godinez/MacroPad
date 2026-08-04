# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from constants import PixelColor

app = {                     # REQUIRED dict, must be named 'app'
  'name' : 'Windows Edge',  # Application name
  'macros' : [              # List of button macros...
    # COLOR    LABEL    KEY SEQUENCE
    # 1st row ----------
    (PixelColor.DARK_GREEN, '< Back', [Keycode.ALT, Keycode.LEFT_ARROW]),
    (PixelColor.DARK_GREEN, 'Fwd >',  [Keycode.ALT, Keycode.RIGHT_ARROW]),
    (PixelColor.DARK_RED,   'Up',     [Keycode.SHIFT, ' ']),      # Scroll up
    # 2nd row ----------
    (PixelColor.OLIVE,    '- Size', [Keycode.CONTROL, Keycode.KEYPAD_MINUS]),
    (PixelColor.OLIVE,    'Size +', [Keycode.CONTROL, Keycode.KEYPAD_PLUS]),
    (PixelColor.DARK_RED, 'Down',   [' ']),                     # Scroll down
    # 3rd row ----------
    (PixelColor.DARK_BLUE, 'Reload',  [Keycode.CONTROL, 'r']),
    (PixelColor.DARK_BLUE, 'Home',    [Keycode.ALT, Keycode.HOME]),
    (PixelColor.DARK_BLUE, 'Private', [Keycode.CONTROL, 'N']),
    # 4th row ----------
    (PixelColor.BLACK,       'Ada', [Keycode.CONTROL, 'n', -Keycode.COMMAND,
                                     'www.adafruit.com\n']),   # Adafruit in new window
    (PixelColor.MAROON,      'Digi', [Keycode.CONTROL, 'n', -Keycode.COMMAND,
                                      'www.digikey.com\n']),   # Digi-Key in new window
    (PixelColor.DARKER_GRAY, 'Hacks', [Keycode.CONTROL, 'n', -Keycode.COMMAND,
                                       'www.hackaday.com\n']), # Hack-a-Day in new win
    # Encoder button ---
    (PixelColor.BLACK, '', [Keycode.CONTROL, 'w']) # Close tab
]
}
