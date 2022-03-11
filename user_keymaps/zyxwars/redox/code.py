print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.tapdance import TapDance
from kmk.modules.split import Split, SplitSide

keyboard = KMKKeyboard()
#keyboard.debug_enabled = True

keyboard.modules.append(Layers())
keyboard.modules.append(ModTap())
keyboard.modules.append(TapDance())

# TODO: Comment out the unwanted side
split_side = SplitSide.LEFT
split_side = SplitSide.RIGHT

split = Split(split_side=split_side, data_pin=board.GP1, data_pin2=board.GP0, split_flip=False, uart_flip=False)
keyboard.modules.append(split)

keyboard.col_pins = [board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8]
keyboard.row_pins = [board.GP10, board.GP11, board.GP12, board.GP13, board.GP14]
keyboard.diode_orientation = DiodeOrientation.COL2ROW

import keymap
keyboard.keymap = keymap.keymap

if __name__ == '__main__':
    print(f'Started {"Left" if split_side else "Right"} side')
    keyboard.go()
