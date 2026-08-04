from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from constants import PixelColor

app = {                    # REQUIRED dict, must be named 'app'
  'name' : 'Delphi 7',     # Application name (20 chars max)
  'macros' : [             # List of button macros...
    # COLOR    LABEL    KEY SEQUENCE
    # 1st row ----------
    (PixelColor.PURPLE, 'Run', [Keycode.F9]),
    (PixelColor.BLACK,       '',    []),
    (PixelColor.BLACK,       '',    []),
    # 2nd row ----------
    (PixelColor.BLACK,    'Grep',  [Keycode.SHIFT, Keycode.ALT, 'S']),
    (PixelColor.DARK_RED, 'Units', [Keycode.CONTROL, Keycode.F12]),
    (PixelColor.BLACK,    'Forms', [Keycode.SHIFT, Keycode.F12]),
    # 3rd row ----------
    (PixelColor.BLACK, '', []),
    (PixelColor.BLACK, '', []),
    (PixelColor.BLACK, '', []),
    # 4th row ----------
    (PixelColor.BLACK,     '', []),
    (PixelColor.DARK_BLUE, '', []),
    (PixelColor.BLACK,     '', []),
    # Encoder button ---
    (PixelColor.BLACK, '', [True]) #boolean = use as light toggle
  ]
}
