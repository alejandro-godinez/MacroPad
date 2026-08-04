# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from constants import PixelColor

app = {                # REQUIRED dict, must be named 'app'
  'name' : 'Numpad', # Application name
  'macros' : [       # List of button macros...
    # COLOR    LABEL    KEY SEQUENCE
    # 1st row ----------
    (PixelColor.OLIVE, '7', ['7']),
    (PixelColor.OLIVE, '8', ['8']),
    (PixelColor.OLIVE, '9', ['9']),
    # 2nd row ----------
    (PixelColor.OLIVE, '4', ['4']),
    (PixelColor.OLIVE, '5', ['5']),
    (PixelColor.OLIVE, '6', ['6']),
    # 3rd row ----------
    (PixelColor.OLIVE, '1', ['1']),
    (PixelColor.OLIVE, '2', ['2']),
    (PixelColor.OLIVE, '3', ['3']),
    # 4th row ----------
    (PixelColor.DARKER_GRAY, '*', ['*']),
    (PixelColor.MAROON,      '0', ['0']),
    (PixelColor.DARKER_GRAY, '#', ['#']),
    # Encoder button ---
    (PixelColor.BLACK, '', [Keycode.BACKSPACE])
]
}
