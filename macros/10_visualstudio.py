from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Visual Studio',# Application name (20 chars max)
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x600060, '<',          [Keycode.CONTROL, 'k', 'p']),
        (0x600060, 'Move Tab V', [Keycode.CONTROL, 'k', 'v']),
        (0x600060, '>',          [Keycode.CONTROL, 'k', 'n']),
        # 2nd row ----------
        (0x600000, 'Pin',        [Keycode.CONTROL, 'p', Keycode.CONTROL, 'p']),
        (0x8B5A00, 'Loc',        [Keycode.CONTROL, '[', 'f']),
        (0x8B5A00, 'Sltn',       [Keycode.CONTROL, '[', 's']),
        # 3rd row ----------
        (0x000060, 'Win',        [Keycode.CONTROL, 'k', Keycode.CONTROL, 'w']),
        (0x000060, '[Bmark]',    [Keycode.CONTROL, 'k', Keycode.CONTROL, 'k']),
        (0x000060, 'Auto',       [Keycode.CONTROL, 'c',                             #copy 
                                  Keycode.CONTROL, 'k', Keycode.CONTROL, 'k',       #bookmark
                                  Keycode.CONTROL, 'k', Keycode.CONTROL, 'w',       #bmark window
                                  Keycode.F2,                                       #rename
                                  Keycode.CONTROL, 'v',                             #past
                                  Keycode.ENTER]),                                  #enter
        # 4th row ----------
        (0x006000, 'Dock',       [Keycode.CONTROL, '[', 'd']),
        (0x006000, 'Float',      [Keycode.CONTROL, '[', 'l']),
        (0x006000, 'Group',      [Keycode.CONTROL, '[', 'm']),
        # Encoder button ---
        (0x000000, '',          [True]) #boolean = use as light toggle
    ]
}
