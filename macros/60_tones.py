# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Tones

# The syntax for Tones in macros is highly peculiar, in order to maintain
# backward compatibility with the original keycode-only macro files.
# The third item for each macro is a list in brackets, and each value within
# is normally an integer (Keycode), float (delay) or string (typed literally).
# Consumer Control codes were added as list-within-list, and then mouse and
# tone further complicate this by adding dicts-within-list. Each tone-related
# item is the key 'tone' with either an integer frequency value, or 0 to stop
# the tone mid-macro (tone is also stopped when key is released).
# Helpful: https://en.wikipedia.org/wiki/Piano_key_frequencies

# This example ONLY shows tones (and delays), but really they can be mixed
# with other elements (keys, codes, mouse) to provide auditory feedback.

from constants import PixelColor

app = {              # REQUIRED dict, must be named 'app'
  'name' : 'Tones',  # Application name
  'macros' : [       # List of button macros...
    # COLOR    LABEL    KEY SEQUENCE
    # 1st row ----------
    (PixelColor.DEEP_RED, 'C3', [{'tone':131}]),
    (PixelColor.OLIVE,    'C4', [{'tone':262}]),
    (PixelColor.LIME,     'C5', [{'tone':523}]),
    # 2nd row ----------
    (PixelColor.DEEP_BLUE_ALT, 'Rising',  [{'tone':131}, 0.2, {'tone':262}, 0.2, {'tone':523}]),
    (PixelColor.BLACK,         '',        []),
    (PixelColor.DEEP_BLUE_ALT, 'Falling', [{'tone':523}, 0.2, {'tone':262}, 0.2, {'tone':131}]),
    # 3rd row ----------
    (PixelColor.BLACK, '', []),
    (PixelColor.BLACK, '', []),
    (PixelColor.BLACK, '', []),
    # 4th row ----------
    (PixelColor.BLACK, '', []),
    (PixelColor.BLACK, '', []),
    (PixelColor.BLACK, '', []),
    # Encoder button ---
    (PixelColor.BLACK, '', [])
 ]
}
