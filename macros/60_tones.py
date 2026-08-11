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
    (PixelColor.WHITE, 'Do',  [{'tone':262}, 0.1]),
    (PixelColor.RED,   'Re',  [{'tone':294}, 0.1]),
    (PixelColor.ORANGE,'Mi',  [{'tone':330}, 0.1]),
    # 2nd row ----------
    (PixelColor.YELLOW,'Fa', [{'tone':349}, 0.1]),
    (PixelColor.GREEN, 'So', [{'tone':392}, 0.1]),
    (PixelColor.CYAN,  'La', [{'tone':440}, 0.1]),
    # 3rd row ----------
    (PixelColor.BLUE,    'Si', [{'tone':493}, 0.1]),
    (PixelColor.MAGENTA, 'Do', [{'tone':523}, 0.1]),
    (PixelColor.BLACK, '', []),
    # 4th row ----------
    (PixelColor.BLACK, '', [{'tone':262}, 0.25, {'tone':294}, 0.25, {'tone':330}, 0.25, {'tone':392}, 1.0, {'tone':523}, 0.25]),  # la cu ca ra ch
    (PixelColor.BLACK, '[Cucaracha]', []),
    (PixelColor.BLACK, '', [{'tone':330}, 0.25, {'tone':392}, 0.25, {'tone':440}, 0.25, {'tone':392}, 0.25, {'tone':349}, 0.25, {'tone':330}, 0.25, {'tone':294}, 0.25]),  # ya no pue de ca mi nar
    # Encoder button ---
    (PixelColor.BLACK, '', [True]) #boolean = use as light toggle
 ]
}
