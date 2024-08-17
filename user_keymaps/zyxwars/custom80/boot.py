import board
import digitalio
import storage
import usb_cdc
import usb_hid
import usb_midi

# Hide circuitpy folder if a specific key is not held on boot
col = digitalio.DigitalInOut(board.GP19)
row = digitalio.DigitalInOut(board.GP5)
col.switch_to_output(value=True)
row.switch_to_input(pull=digitalio.Pull.DOWN)

if not row.value:
    storage.disable_usb_drive()
    # Equivalent to usb_cdc.enable(console=False, data=False)
    usb_cdc.disable()
    usb_midi.disable()
    # https://docs.circuitpython.org/en/latest/shared-bindings/usb_hid/index.html
    usb_hid.enable(boot_device=1)

row.deinit()
col.deinit()
