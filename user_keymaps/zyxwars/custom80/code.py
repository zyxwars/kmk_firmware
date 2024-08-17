print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())

from kmk.modules.layers import Layers
keyboard.modules.append(Layers())


keyboard.col_pins = (board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP12,board.GP13,board.GP14,board.GP15,board.GP16,board.GP17,board.GP18,board.GP19,board.GP20)
keyboard.row_pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
    KC.ESC,    KC.F1,    KC.F2,   KC.F3,   KC.F4, KC.F5,    KC.F6, KC.F7,    KC.F8,   KC.F9,    KC.F10,    KC.F11,      KC.F12,      KC.CAPS,    KC.DEL,
    KC.GRAVE,  KC.N1,    KC.N2,   KC.N3,   KC.N4, KC.N5,    KC.N6, KC.N7,    KC.N8,   KC.N9,    KC.N0,     KC.MINUS,    KC.EQUAL,    KC.BSPC,    KC.NO,
    KC.TAB,    KC.Q,     KC.W,    KC.E,    KC.R,  KC.T,     KC.Y,  KC.U,     KC.I,    KC.O,     KC.P,      KC.LBRACKET, KC.RBRACKET, KC.BSLASH,  KC.NO,
    KC.BSPC,   KC.A,     KC.S,    KC.D,    KC.F,  KC.G,     KC.H,  KC.J,     KC.K,    KC.L,     KC.SCOLON, KC.QUOTE,    KC.NO,       KC.ENTER,   KC.NO,
    KC.LSHIFT, KC.NO,    KC.Z,    KC.X,    KC.C,  KC.V,     KC.B,  KC.N,     KC.M,    KC.COMMA, KC.DOT,    KC.SLASH,    KC.RSHIFT,   KC.NO,      KC.NO,
    KC.LCTRL,  KC.MO(1), KC.LGUI, KC.LALT, KC.NO, KC.SPACE, KC.NO, KC.SPACE, KC.LEFT, KC.DOWN,  KC.UP,     KC.RIGHT,    KC.RCTRL,    KC.MO(1),   KC.NO
    ]
    ,
    [
    KC.TRNS,   KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MPRV, KC.MPLY, KC.MNXT, KC.MUTE, KC.VOLD, KC.VOLU, KC.TRNS,    KC.TRNS,   KC.TRNS,
    KC.TRNS,   KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,    KC.TRNS,   KC.TRNS,
    KC.TRNS,   KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,    KC.TRNS,   KC.TRNS,
    KC.TRNS,   KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,    KC.TRNS,   KC.TRNS,
    KC.TRNS,   KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,    KC.TRNS,   KC.TRNS,
    KC.TRNS,   KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,    KC.TRNS,   KC.TRNS
    ]
]

if __name__ == '__main__':
    keyboard.go()


