from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values


app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Outlook',          # Application name (20 chars max)
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x400040, '<',          [Keycode.CONTROL, ',']),
        (0x400040, 'Select',     [Keycode.CONTROL, Keycode.SPACE]),
        (0x400040, '>',          [Keycode.CONTROL, '.']),
        # 2nd row ----------
        (0x006000, 'Read',       [Keycode.CONTROL, 'q']),
        (0x000000, '',           []),
        (0x8B5A00, 'UnRead',     [Keycode.CONTROL, 'u']),
        # 3rd row ----------
        (0x000060, 'Move',       [Keycode.CONTROL, Keycode.SHIFT, 'v']),
        (0x000000, '',           []),
        (0x600000, 'Delete',     [Keycode.DELETE]),
        # 4th row ----------
        (0x000000, '',          []),
        (0x000000, '',          []),
        (0x000000, '',          []),
        # Encoder button ---
        (0x000000, '',          [True]) #boolean = use as light toggle
    ]
}
