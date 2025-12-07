import board
import digitalio
import storage
import usb_cdc

# Setup the top-left key (KEY1) as the trigger
# The keys on the Macropad are switches that connect to ground when pressed.
# We use a Pull Up so the value is True when NOT pressed, and False when pressed.
button = digitalio.DigitalInOut(board.KEY1)
button.pull = digitalio.Pull.UP

# Logic:
# If button.value is True (Not Pressed), we DISABLE the drive.
# If button.value is False (Pressed), we do nothing (Drive stays enabled).
if button.value:
    storage.disable_usb_drive()
    # Optional: Uncomment the line below if you also want to hide the Serial/COM port
    # usb_cdc.disable()
else:
    # Visual feedback: You could blink the LED here if you wanted,
    # but the drive appearing on your desktop is the best feedback.
    pass
