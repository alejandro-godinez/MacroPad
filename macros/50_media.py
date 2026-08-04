# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Consumer Control codes (media keys)

# The syntax for Consumer Control macros is a little peculiar, in order to
# maintain backward compatibility with the original keycode-only macro files.
# The third item for each macro is a list in brackets, and each value within
# is normally an integer (Keycode), float (delay) or string (typed literally).
# Consumer Control codes are distinguished by enclosing them in a list within
# the list, which is why you'll see double brackets [[ ]] below.
# Like Keycodes, Consumer Control codes can be positive (press) or negative
# (release), and float values can be inserted for pauses.

# To reference Consumer Control codes, import ConsumerControlCode like so...
from adafruit_hid.consumer_control_code import ConsumerControlCode
from constants import PixelColor
# You can still import Keycode as well if a macro file mixes types!
# See other macro files for typical Keycode examples.

app = {              # REQUIRED dict, must be named 'app'
  'name' : 'Media',  # Application name
  'macros' : [       # List of button macros...
    # COLOR    LABEL    KEY SEQUENCE
    # 1st row ----------
    (PixelColor.BLACK,         '',        []),
    (PixelColor.DEEP_BLUE_ALT, 'Vol+',    [[ConsumerControlCode.VOLUME_INCREMENT]]),
    (PixelColor.DARK_GRAY,     'Bright+', [[ConsumerControlCode.BRIGHTNESS_INCREMENT]]),
    # 2nd row ----------
    (PixelColor.BLACK,         '',        []),
    (PixelColor.DEEP_BLUE_ALT, 'Vol-',    [[ConsumerControlCode.VOLUME_DECREMENT]]),
    (PixelColor.DARK_GRAY,     'Bright-', [[ConsumerControlCode.BRIGHTNESS_DECREMENT]]),
    # 3rd row ----------
    (PixelColor.BLACK,    '',     []),
    (PixelColor.DEEP_RED, 'Mute', [[ConsumerControlCode.MUTE]]),
    (PixelColor.BLACK,    '',     []),
    # 4th row ----------
    (PixelColor.OLIVE, '<<',         [[ConsumerControlCode.SCAN_PREVIOUS_TRACK]]),
    (PixelColor.LIME,  'Play/Pause', [[ConsumerControlCode.PLAY_PAUSE]]),
    (PixelColor.OLIVE, '>>',         [[ConsumerControlCode.SCAN_NEXT_TRACK]]),
    # Encoder button ---
    (PixelColor.BLACK, '', [])
  ]
}
