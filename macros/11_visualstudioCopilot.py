from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from constants import PixelColor

app = {                        # REQUIRED dict, must be named 'app'
  'name' : 'VS Copilot/Test',  # Application name (20 chars max)
  'macros' : [                 # List of button macros...
    # COLOR    LABEL    KEY SEQUENCE
    # 1st row ----------
    (PixelColor.DEEP_BLUE, 'CMPLT',     [Keycode.CONTROL, 'k', Keycode.CONTROL, Keycode.SHIFT, 'c']),
    (PixelColor.DEEP_BLUE, '[toggle]',  []),
    (PixelColor.DEEP_BLUE, 'NES',       [Keycode.CONTROL, 'k', Keycode.CONTROL, Keycode.SHIFT, 'n']),
    # 2nd row ----------
    (PixelColor.DEEP_GREEN, 'Ask',  [Keycode.ALT, '/']),
    (PixelColor.DEEP_GREEN, 'Chat', [Keycode.CONTROL, '\\', Keycode.CONTROL, 'c']),
    (PixelColor.BLACK,      '',     []),
    # 3rd row ----------
    (PixelColor.BLACK, '', []),
    (PixelColor.BLACK, '', []),
    (PixelColor.BLACK, '', []),
    # 4th row ----------
    (PixelColor.DEEP_RED, 'Win',    [Keycode.CONTROL, 'e', 't']),
    (PixelColor.BLACK,    '[TEST]', []),
    (PixelColor.DEEP_RED, 'RunAll', [Keycode.CONTROL, 'r', 'a']),
    # Encoder button ---
    (PixelColor.BLACK, '', [True]) #boolean = use as light toggle
  ]
}
