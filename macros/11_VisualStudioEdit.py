from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Visual Studio EDIT',          # Application name (20 chars max)
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x006000, 'TABs',        [Keycode.CONTROL, 'r', Keycode.ALT, 't']),
        (0x000060, 'SPCs',        [Keycode.CONTROL, 'r', Keycode.ALT, 's']),
        (0x600060, 'Usings',      [Keycode.CONTROL, 'r', 'g']),
        # 2nd row ----------
        (0x000000, 'Doc',         [Keycode.CONTROL, 'k', Keycode.CONTROL, 'd']),
        (0x000000, '[Format]',    []),
        (0x000000, 'Sel',         [Keycode.CONTROL, 'k', Keycode.CONTROL, 'f']),
        # 3rd row ----------
        (0x000000, '',          []),
        (0x000000, '',          []),
        (0x000000, '',          []),
        # 4th row ----------
        (0x000000, '',          []),
        (0x000000, '',          []),
        (0x000000, '',          []),
        # Encoder button ---
        (0x000000, '',          [])
    ]
}
