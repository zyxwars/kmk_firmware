import board

from kmk.consts import DiodeOrientation
from kmk.mcus.circuitpython_samd21 import Firmware
from kmk.pins import Pin as P

keyboard = Firmware()

keyboard.col_pins = (P.RX, P.A1, P.A2, P.A3, P.A4, P.A5)
keyboard.row_pins = (P.D13, P.D11, P.D10, P.D9, P.D7)
keyboard.diode_orientation = DiodeOrientation.COLUMNS

keyboard.split_type = "UART"
keyboard.split_flip = True
keyboard.split_offsets = [6, 6, 6, 6, 6]
keyboard.uart_pin = board.SDA
keyboard.extra_data_pin = board.SCL

# ------------------User level config variables ---------------------------------------
keyboard.debug_enabled = True

# ---------------------- Keymap ---------------------------------------------------------


if __name__ == '__main__':
    keyboard.go()
