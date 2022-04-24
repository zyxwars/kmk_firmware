from kmk.keys import KC
from kmk.handlers.sequences import send_string, simple_key_sequence

# Convenience
_______ = KC.TRNS
S = KC.LSFT
# KC.RCBR causes pystack error, when used in layer ???
LCBC = S(KC.LBRC)
RCBC = S(KC.RBRC)

# Layers
FN = KC.MO(1)
ENTFN = KC.LT(1, KC.ENT, prefer_hold=True, tap_interrupted=False)
GAMING = KC.TG(2)

# Mod tap
SFTMOD1 = KC.MT(KC.ESC, KC.LSFT, prefer_hold=True, tap_interrupted=False)
SFTMOD2 = KC.MT(KC.BSLS, KC.RSFT, prefer_hold=True, tap_interrupted=False)

# Tap dance
BSPCMOD = KC.TD(KC.BSPC, KC.LCTL(KC.BSPC))
F5RUN = KC.TD(KC.F5, KC.LCTL(KC.F5))
NXTPRV = KC.TD(KC.MNXT, KC.MPRV)

# CLOSE = KC.LALT(KC.F4)
# FILES = KC.LGUI(KC.E)

# Macros
SLEEP = simple_key_sequence(
    (
        KC.LGUI(KC.X),
        KC.U,
        KC.S,
    )
)
GITCA = simple_key_sequence(
    (
        send_string('git add -A'),
        KC.ENT,
        send_string('git commit -m '),
        KC.LSFT(KC.QUOT),
        KC.LSFT(KC.QUOT),
        KC.LEFT,
    )
)



keymap = [
    [   # COLEMAK-DH
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   F5RUN,          GAMING,  KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.BSLS,
        KC.TAB,  KC.Q,    KC.W,    KC.F,    KC.P,    KC.B,    KC.F12,         _______, KC.J,    KC.L,    KC.U,    KC.Y,    KC.SCLN, KC.EQUAL,
        BSPCMOD, KC.A,    KC.R,    KC.S,    KC.T,    KC.G,    GITCA,          _______, KC.M,    KC.N,    KC.E,    KC.I,    KC.O,    KC.QUOT,
        SFTMOD1, KC.Z,    KC.X,    KC.C,    KC.D,    KC.V,    KC.RESET,       _______, KC.K,    KC.H,    KC.COMMA, KC.DOT,  KC.SLASH,SFTMOD2,
        KC.LCTL, KC.LGUI, KC.LALT, KC.DEL,  FN,      KC.SPC,  KC.LSFT,        _______, ENTFN,   FN,      KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT
    ],
    #[   # FN
    #   _______, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   _______,        _______, KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,
    #   _______, S(KC.N1),S(KC.N2),S(KC.N3),S(KC.N4),S(KC.N5),_______,        _______, S(KC.N6),S(KC.N7),S(KC.N8),_______, KC.PLUS, KC.F12,
    #   _______, KC.MINUS,KC.EQUAL,LCBC,    KC.LPRN, KC.LBRC, _______,        _______, KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT,KC.UNDS, _______,
    #   _______, _______, _______, RCBC,    KC.RPRN, KC.RBRC, _______,        _______, _______, _______, _______, _______, _______, _______,
    #   _______, _______, _______, _______, _______, _______, _______,        _______, _______, _______, KC.MPLY, KC.VOLD, KC.VOLU, NXTPRV,
    #],
    [   # PROGRAMMER COLEMAK FN
        _______, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   _______,        _______, KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,
        _______, S(KC.N1),S(KC.N2),S(KC.N3),S(KC.N4),S(KC.N5),_______,        _______, S(KC.N6),S(KC.N7),S(KC.N8),KC.PLUS, KC.GRV,  KC.F12,
        _______, KC.LBRC, KC.EQUAL,LCBC,    KC.LPRN, KC.MINUS,_______,        _______, KC.UNDS,KC.DOWN, KC.UP,   KC.UNDS, KC.RBRC, _______,
        _______, KC.RBRC, KC.PLUS, RCBC,    KC.RPRN, _______, _______,        _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, _______,        _______, _______, _______, KC.MPLY, KC.VOLD, KC.VOLU, NXTPRV,
    ],
    [   # GAMING/QWERTY
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,          GAMING,  KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   _______,
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.H,           KC.RBRC, KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    _______,
        KC.BSPC, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.M,           _______, KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, _______,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    _______,        _______, KC.N,    KC.M,    KC.COMMA, KC.DOT, KC.SLASH,_______,
        _______, _______, _______, _______, _______,  _______,_______,        _______, _______, _______, _______, _______, _______, _______,
    ],
]
