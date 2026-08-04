from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from constants import PixelColor

app = {                          # REQUIRED dict, must be named 'app'
  'name' : 'Microsoft SQL SMS',  # Application name (20 chars max)
  'macros' : [                   # List of button macros...
    # COLOR    LABEL    KEY SEQUENCE
    # 1st row ----------
    (PixelColor.PURPLE, '<',          [Keycode.CONTROL, 'k', 'p']),
    (PixelColor.PURPLE, 'Move Tab V', [Keycode.CONTROL, 'k', 'v']),
    (PixelColor.PURPLE, '>',          [Keycode.CONTROL, 'k', 'n']),
    # 2nd row ----------
    (PixelColor.BLACK,    'Pin',   [Keycode.CONTROL, 'p', Keycode.CONTROL, 'p']),
    (PixelColor.DARK_RED, 'SnipM', [Keycode.CONTROL, 'K', Keycode.CONTROL, 'X']),
    (PixelColor.BLACK,    'Snip+', [Keycode.CONTROL, 'K', Keycode.CONTROL, 'B']),
    # 3rd row ----------
    (PixelColor.DARK_GREEN, 'UCase',  [Keycode.CONTROL, Keycode.SHIFT, 'u']),
    (PixelColor.DARK_GREEN, 'LCase',  [Keycode.CONTROL, 'u']),
    (PixelColor.LIGHT_GRAY, 'WSpace', [Keycode.CONTROL, 'r', Keycode.CONTROL, 'w']),
    # 4th row ----------
    (PixelColor.DARK_BLUE, 'Re-Cache',  [Keycode.CONTROL, Keycode.SHIFT, 'r']),
    (PixelColor.BLACK,     '',          []),
    (PixelColor.DARK_BLUE, 'Duplicate', [Keycode.CONTROL,'a',   #select all
                                         Keycode.CONTROL,'c',   #copy
                                         Keycode.CONTROL,'n',   #new query
                                         Keycode.CONTROL,'v']), #paste
    # Encoder button ---
    (PixelColor.BLACK, '', [True]) #boolean = use as light toggle
  ]
}
