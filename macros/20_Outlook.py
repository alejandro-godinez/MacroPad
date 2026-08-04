from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from constants import PixelColor


app = {                    # REQUIRED dict, must be named 'app'
  'name' : 'Outlook',      # Application name (20 chars max)
  'macros' : [             # List of button macros...
    # COLOR    LABEL    KEY SEQUENCE
    # 1st row ----------
    (PixelColor.PURPLE, '<',      [Keycode.CONTROL, ',']),
    (PixelColor.PURPLE, 'Select', [Keycode.CONTROL, Keycode.SPACE]),
    (PixelColor.PURPLE, '>',      [Keycode.CONTROL, '.']),
    # 2nd row ----------
    (PixelColor.DEEP_GREEN, 'Read',   [Keycode.CONTROL, 'q']),
    (PixelColor.BLACK,      '',       []),
    (PixelColor.BROWN,      'UnRead', [Keycode.CONTROL, 'u']),
    # 3rd row ----------
    (PixelColor.DEEP_BLUE, 'Move',   [Keycode.CONTROL, Keycode.SHIFT, 'v']),
    (PixelColor.BLACK,     '',       []),
    (PixelColor.DEEP_RED,  'Delete', [Keycode.DELETE]),
    # 4th row ----------
    (PixelColor.BLACK, '', []),
    (PixelColor.BLACK, '', []),
    (PixelColor.BLACK, '', []),
    # Encoder button ---
    (PixelColor.BLACK, '', [True]) #boolean = use as light toggle
  ]
}
