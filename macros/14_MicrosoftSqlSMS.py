from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Microsoft SQL SMS',          # Application name (20 chars max)
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x400040, '<',          [Keycode.CONTROL, 'k', 'p']),
        (0x400040, 'Move Tab V', [Keycode.CONTROL, 'k', 'v']),
        (0x400040, '>',          [Keycode.CONTROL, 'k', 'n']),
        # 2nd row ----------
        (0x000000, 'Pin',        [Keycode.CONTROL, 'p', Keycode.CONTROL, 'p']),
        (0x400000, 'SnipM',      [Keycode.CONTROL, 'K', Keycode.CONTROL, 'X']),
        (0x000000, 'Snip+',      [Keycode.CONTROL, 'K', Keycode.CONTROL, 'B']),
        # 3rd row ----------
        (0x004000, 'UCase',      [Keycode.CONTROL, Keycode.SHIFT, 'u']),
        (0x004000, 'LCase',      [Keycode.CONTROL, 'u']),
        (0xF0F0F0, 'WSpace',     [Keycode.CONTROL, 'r', Keycode.CONTROL, 'w']),
        # 4th row ----------
        (0x000000, '',               []),
        (0x000040, 'Refresh Cache',  [Keycode.CONTROL, Keycode.SHIFT, 'r']),
        (0x000000, '',               []),
        # Encoder button ---
        (0x000000, '',               [True]) #boolean = use as light toggle
    ]
}
