# SPDX-FileCopyrightText: 2021 Victor Toni - GitHub @vitoni
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: blank screen for idle

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'VisualStudio Copilot',# Application name (20 chars max)
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000060, 'CMPLT',      [Keycode.CONTROL, 'k', Keycode.CONTROL, Keycode.SHIFT, 'c']),
        (0x000060, '[toggle]',   []),
        (0x000060, 'NES',        [Keycode.CONTROL, 'k', Keycode.CONTROL, Keycode.SHIFT, 'c']),
        # 2nd row ----------
        (0x006000, 'Ask',        [Keycode.ALT, '/']),
        (0x006000, 'Chat',       [Keycode.CONTROL, '\\', Keycode.CONTROL, Keycode.SHIFT, 'n']),
        (0x000000, '',           []),
        # 3rd row ----------
        (0x000000, '',           []),
        (0x000000, '',           []),
        (0x000000, '',           []),
        # 4th row ----------
        (0x000000, '',           []),
        (0x000000, '',           []),
        (0x000000, '',           []),
        # Encoder button ---
        (0x000000, '',          [True]) #boolean = use as light toggle
    ]
}
