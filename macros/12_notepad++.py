from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from constants import PixelColor

app = {                  # REQUIRED dict, must be named 'app'
  'name' : 'Notepad++',  # Application name (20 chars max)
  'macros' : [           # List of button macros...
    # COLOR    LABEL    KEY SEQUENCE
    # 1st row ----------
    (PixelColor.PURPLE, 'MoveTab', [Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, 'v']),
    (PixelColor.PURPLE, 'Fld',     [Keycode.ALT, '0']),
    (PixelColor.PURPLE, 'UFld',    [Keycode.ALT, Keycode.SHIFT, '0']),
    # 2nd row ----------
    (PixelColor.LIME,       'UCase',  [Keycode.CONTROL, Keycode.SHIFT, 'u']),
    (PixelColor.LIME,       'LCase',  [Keycode.CONTROL, 'u']),
    (PixelColor.LIGHT_GRAY, 'SpcTab', [Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, Keycode.TAB]),
    # 3rd row ----------
    (PixelColor.BRIGHT_BLUE, 'Compare', [Keycode.CONTROL, Keycode.ALT, 'c']),
    (PixelColor.ORANGE,      '[clr]',   [Keycode.CONTROL, Keycode.ALT, 'x']),
    (PixelColor.BRIGHT_BLUE, 'VSync',   [Keycode.CONTROL, Keycode.SHIFT, 'v']),
    # 4th row ----------
    (PixelColor.BROWN,  'Dir',    [Keycode.CONTROL, Keycode.SHIFT, 'e']),
    (PixelColor.BLUE,   'Align',  [Keycode.CONTROL, Keycode.SHIFT, '=']),
    (PixelColor.INDIGO, 'JSFrmt', [Keycode.CONTROL, Keycode.ALT, 'm']),
    # Encoder button ---
    (PixelColor.BLACK, '', [True]) #boolean = use as light toggle
  ]
}
