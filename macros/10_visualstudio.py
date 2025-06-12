# SPDX-FileCopyrightText: 2021 Victor Toni - GitHub @vitoni
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: blank screen for idle

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Visual Studio',# Application name (20 chars max)
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x400040, '<',          [Keycode.CONTROL, 'k', 'p']),
        (0x400040, 'Move Tab V', [Keycode.CONTROL, 'k', 'v']),
        (0x400040, '>',          [Keycode.CONTROL, 'k', 'n']),
        # 2nd row ----------
        (0x000000, '',          []),
        (0x400000, 'Pin',   [Keycode.CONTROL, 'p', Keycode.CONTROL, 'p']),
        (0x000000, '',          []),
        # 3rd row ----------
        (0x8B5A00, 'Loc',       [Keycode.CONTROL, '[', 'f']),
        (0x000000, '[File]',  []),
        (0x8B5A00, 'Sltn',    [Keycode.CONTROL, '[', 's']),
        # 4th row ----------
        (0x000060, 'Win',       [Keycode.CONTROL, 'k', Keycode.CONTROL, 'w']),
        (0x000060, 'Bmark',  [Keycode.CONTROL, 'k', Keycode.CONTROL, 'k']),
        (0x004000, 'Copilot',   [Keycode.CONTROL, 'k', Keycode.CONTROL, Keycode.SHIFT, 'c']),
        # Encoder button ---
        (0x000000, '',          [True]) #boolean = use as light toggle
    ]
}
