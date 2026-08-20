from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values


app = {                    # REQUIRED dict, must be named 'app'
  'name' : 'Webex',        # Application name (20 chars max)
  'macros' : [             # List of button macros...
    # COLOR    LABEL    KEY SEQUENCE
    # 1st row ----------
    (0x00F000, 'Answer',     [Keycode.CONTROL, Keycode.SHIFT, 'C']),
    (0x202000, 'End',        [Keycode.CONTROL, 'L']),
    (0x800000, 'Decline',    [Keycode.CONTROL, 'D']),
    # 2nd row ----------
    (0x000060, 'Mute',       [Keycode.CONTROL, 'm']),                 # toggle mute on call
    (0xF0F0F0, '[VIDEO]',    [Keycode.CONTROL, Keycode.SHIFT, 'v']),  # toggle video on call
    (0x000060, '[Chat]',     [Keycode.CONTROL, 'e']),                 # toggle chat pane
    # 3rd row ----------
    (0x600060, 'Share',      [Keycode.CONTROL, Keycode.SHIFT, 'd']),  # start share
    (0x202000, 'Stop',       [Keycode.CONTROL, Keycode.SHIFT, 'z']),  # stop sharing
    (0x000000, '',           [Keycode.CONTROL, Keycode.ALT, 'p']),    # Show/Hide video view while sharing
    # 4th row ----------
    (0x600060, 'Annotate',   [Keycode.ALT, Keycode.SHIFT, 'z']), # start annotation
    (0x202000, 'End',        [Keycode.ALT, Keycode.SHIFT, 'x']), # end annotation
    (0x000000, '',           []),
    # Encoder button ---
    (0x000000, '',          [True]) #boolean = use as light toggle
    ]
}
