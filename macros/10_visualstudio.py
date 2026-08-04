from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from constants import PixelColor

app = {                      # REQUIRED dict, must be named 'app'
  'name' : 'Visual Studio',  # Application name (20 chars max)
  'macros' : [               # List of button macros...
    # COLOR    LABEL    KEY SEQUENCE
    # 1st row ----------
    (PixelColor.DEEP_PURPLE, '<',          [Keycode.CONTROL, 'k', 'p']),
    (PixelColor.DEEP_PURPLE, 'Move Tab V', [Keycode.CONTROL, 'k', 'v']),
    (PixelColor.DEEP_PURPLE, '>',          [Keycode.CONTROL, 'k', 'n']),
    # 2nd row ----------
    (PixelColor.DEEP_RED, 'Pin',  [Keycode.CONTROL, 'p', Keycode.CONTROL, 'p']),
    (PixelColor.BROWN,    'Loc',  [Keycode.CONTROL, '[', 'f']),
    (PixelColor.BROWN,    'Sltn', [Keycode.CONTROL, '[', 's']),
    # 3rd row ----------
    (PixelColor.DEEP_BLUE, 'Win',     [Keycode.CONTROL, 'k', Keycode.CONTROL, 'w']),
    (PixelColor.DEEP_BLUE, '[Bmark]', [Keycode.CONTROL, 'k', Keycode.CONTROL, 'k']),
    (PixelColor.DEEP_BLUE, 'Auto',    [Keycode.CONTROL, 'c',                             #copy 
                                       Keycode.CONTROL, 'k', Keycode.CONTROL, 'k',       #bookmark
                                       Keycode.CONTROL, 'k', Keycode.CONTROL, 'w',       #bmark window
                                       Keycode.F2,                                       #rename
                                       Keycode.CONTROL, 'v',                             #past
                                       Keycode.ENTER]),                                  #enter
    # 4th row ----------
    (PixelColor.DEEP_GREEN, 'Dock',  [Keycode.CONTROL, '[', 'd']),
    (PixelColor.DEEP_GREEN, 'Float', [Keycode.CONTROL, '[', 'l']),
    (PixelColor.DEEP_GREEN, 'Group', [Keycode.CONTROL, '[', 'm']),
    # Encoder button ---
    (PixelColor.BLACK, '', [True]) #boolean = use as light toggle
  ]
}
