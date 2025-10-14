from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Delphi 7',     # Application name (20 chars max)
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x400040, 'Run',     [Keycode.F9]),
        (0x400040, '',        []),
        (0x400040, '',        []),
        # 2nd row ----------
        (0x000000, 'Grep',    [Keycode.SHIFT, Keycode.ALT, 'S']),
        (0x400000, 'Units',   [Keycode.CONTROL, Keycode.F12]),
        (0x000000, 'Forms',   [Keycode.SHIFT, Keycode.F12]),
        # 3rd row ----------
        (0x004000, '',        []),
        (0x004000, '',        []),
        (0xF0F0F0, '',        []),
        # 4th row ----------
        (0x000000, '',        []),
        (0x000040, '',        []),
        (0x000000, '',        []),
        # Encoder button ---
        (0x000000, '',        [True]) #boolean = use as light toggle
    ]
}
