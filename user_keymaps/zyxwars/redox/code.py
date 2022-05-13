print("Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.tapdance import TapDance
from kmk.modules.split import Split, SplitSide
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.capsword import CapsWord
from kmk.keys import KC, make_key


keyboard = KMKKeyboard()
#keyboard.debug_enabled = True

combos = Combos()
keyboard.modules.append(combos)
GUI_COMBO_TIMEOUT = 200
# This can be remade into a layer if the timeout proves to be annoying
# Make key the on press and the layer equivalent of the combos on hold and set prefer_hold = True
combos.combos = [
    Sequence((KC.LGUI, KC.C), KC.LALT(KC.F4), timeout=GUI_COMBO_TIMEOUT),
    # This is for Windows as WIN + E opens file manager, which makes more sense as WIN + F
    # And changing Windows shortcuts is much more cumbersome that doing it here
    Sequence((KC.LGUI, KC.F), KC.LGUI(KC.E), timeout=GUI_COMBO_TIMEOUT)
]

tapdance = TapDance()
tapdance.tap_time = 100
keyboard.modules.append(tapdance)

keyboard.modules.append(CapsWord())
keyboard.modules.append(ModTap())
keyboard.modules.append(Layers())

# TODO: Comment out the unwanted side
split_side = SplitSide.LEFT
split_side = SplitSide.RIGHT

split = Split(split_side=split_side, data_pin=board.GP1,
              data_pin2=board.GP0, split_flip=False, uart_flip=False)
keyboard.modules.append(split)

keyboard.col_pins = [board.GP2, board.GP3, board.GP4,
                     board.GP5, board.GP6, board.GP7, board.GP8]
keyboard.row_pins = [board.GP10, board.GP11, board.GP12, board.GP13, board.GP14]
keyboard.diode_orientation = DiodeOrientation.COL2ROW

import keymap
keyboard.keymap = keymap.keymap

if __name__ == '__main__':
    print(f'Started {"Left" if split_side == SplitSide.LEFT else "Right"} side')
    keyboard.go()
