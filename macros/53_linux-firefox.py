# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Firefox web browser for Linux

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from constants import PixelColor

app = {                      # REQUIRED dict, must be named 'app'
  'name' : 'Linux Firefox',  # Application name
  'macros' : [               # List of button macros...
    # COLOR    LABEL    KEY SEQUENCE
    # 1st row ----------
    (PixelColor.DARK_GREEN, '< Back', [Keycode.CONTROL, '[']),
    (PixelColor.DARK_GREEN, 'Fwd >',  [Keycode.CONTROL, ']']),
    (PixelColor.DARK_RED,   'Up',     [Keycode.SHIFT, ' ']),      # Scroll up
    # 2nd row ----------
    (PixelColor.OLIVE,    '< Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
    (PixelColor.OLIVE,    'Tab >', [Keycode.CONTROL, Keycode.TAB]),
    (PixelColor.DARK_RED, 'Down',  [' ']),                     # Scroll down
    # 3rd row ----------
    (PixelColor.DARK_BLUE, 'Reload',  [Keycode.CONTROL, 'r']),
    (PixelColor.DARK_BLUE, 'Home',    [Keycode.CONTROL, 'h']),
    (PixelColor.DARK_BLUE, 'Private', [Keycode.CONTROL, Keycode.SHIFT, 'p']),
    # 4th row ----------
    (PixelColor.DARKER_GRAY, 'Ada', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                                     'www.adafruit.com\n']), # adafruit.com in a new tab
    (PixelColor.DARK_BLUE,   'Dev Mode', [Keycode.F12]),     # dev mode
    (PixelColor.DARKER_GRAY, 'Digi', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                                      'digikey.com\n']),     # digikey in a new tab
    # Encoder button ---
    (PixelColor.BLACK, '', [Keycode.CONTROL, 'w']) # Close window/tab
  ]
}
