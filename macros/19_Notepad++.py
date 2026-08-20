from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Notepad++',          # Application name (20 chars max)
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x400040, 'MoveTab', [Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, 'v']),
        (0x400040, 'Fld',     [Keycode.ALT, '0']),
        (0x400040, 'UFld',    [Keycode.ALT, Keycode.SHIFT, '0']),
        # 2nd row ----------
        (0x00F000, 'UCase',   [Keycode.CONTROL, Keycode.SHIFT, 'u']),
        (0x00F000, 'LCase',   [Keycode.CONTROL, 'u']),
        (0xF0F0F0, 'SpcTab',  [Keycode.CONTROL, Keycode.ALT, Keycode.SHIFT, Keycode.TAB]),
        # 3rd row ----------
        (0x0000F0, 'Compare', [Keycode.CONTROL, Keycode.ALT, 'c']),
        (0xF06040, '[clr]',   [Keycode.CONTROL, Keycode.ALT, 'x']),
        (0x0000F0, 'VSync',   [Keycode.CONTROL, Keycode.SHIFT, 'v']),
        # 4th row ----------
        (0x8B5A00, 'Dir',     [Keycode.CONTROL, Keycode.SHIFT, 'e']),
        (0x0000FF, 'Align',   [Keycode.CONTROL, Keycode.SHIFT, '=']),
        (0x6000FF, 'JSFrmt',  [Keycode.CONTROL, Keycode.ALT, 'm']),
        # Encoder button ---
        (0x000000, '',        [True]) #boolean = use as light toggle
    ]
}
