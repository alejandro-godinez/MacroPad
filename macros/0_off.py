# MACROPAD Hotkeys: blank screen for idle with off indicator

from constants import PixelColor

app = {                    # REQUIRED dict, must be named 'app'
  'name' : 'OFF',          # Application name (20 chars max)
  'macros' : [             # List of button macros...
    # COLOR    LABEL    KEY SEQUENCE
    # 1st row ----------
    (PixelColor.BLACK, '', []),
    (PixelColor.BLACK, '', []),
    (PixelColor.BLACK, '', []),
    # 2nd row ----------
    (PixelColor.BLACK, '', []),
    (PixelColor.BLACK, '', []),
    (PixelColor.BLACK, '', []),
    # 3rd row ----------
    (PixelColor.BLACK, '', []),
    (PixelColor.BLACK, '', []),
    (PixelColor.BLACK, '', []),
    # 4th row ----------
    (PixelColor.BLACK, '', []),
    (PixelColor.BLACK, '', []),
    (PixelColor.BLACK, '', []),
    # Encoder button ---
    (PixelColor.BLACK, '', [])
]
}
