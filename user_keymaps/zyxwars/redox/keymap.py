from kmk.keys import KC
from kmk.handlers.sequences import send_string, simple_key_sequence

_______ = KC.TRNS
S = KC.LSFT
# KC.RCBR causes pystack error, when used in layer ???
LCBC = S(KC.LBRC)
RCBC = S(KC.RBRC)

# Layers
GUI = KC.LM(2, KC.LGUI)
FN = KC.MO(1)
ENTFN = KC.LT(1, KC.ENT, prefer_hold=True, tap_interrupted=False)
GAMING = KC.TG(3)

# Multi
SFTMOD1 = KC.LT(4, KC.ESC, prefer_hold=True, tap_interrupted=False)
SFTMOD2 = KC.LT(4, S(KC.MINUS), prefer_hold=True, tap_interrupted=False)
F5RUN = KC.TD(KC.F5, KC.LCTL(KC.F5))
NXTPRV = KC.TD(KC.MNXT, KC.MPRV)

CLOSE = KC.LALT(KC.F4)
FILES = KC.LGUI(KC.E)
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
    #[   # QWERTY
    #    KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,  KC.N5,  F5RUN,          GAMING,  KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINUS,
    #    KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,   KC.T,   KC.LBRC,        KC.RBRC, KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.EQUAL,
    #    KC.BSPC, KC.A,    KC.S,    KC.D,    KC.F,   KC.G,   GITCA,          _______, KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,
    #    SFTESC,  KC.Z,    KC.X,    KC.C,    KC.V,   KC.B,   KC.RESET,       _______, KC.N,    KC.M,    KC.COMMA,KC.DOT,  KC.SLASH,SFTBSLS,
    #    KC.LCTL, GUI,     KC.LALT, KC.F12,  FN,     KC.SPC, KC.DEL,         ENTFN,   ENTFN,   FN,      KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT
    #],
    [   # COLEMAK-DH
        S(KC.GRV),S(KC.N1),S(KC.N2),S(KC.N3),S(KC.N4),S(KC.N5),F5RUN,         GAMING,  S(KC.N6), S(KC.N7),S(KC.N8),S(KC.N9),S(KC.N0),S(KC.BSLS),
        KC.TAB,  KC.Q,    KC.W,    KC.F,    KC.P,    KC.B,    KC.F12,         _______, KC.J,    KC.L,    KC.U,    KC.Y,    KC.SCLN, KC.EQUAL,
        KC.BSPC, KC.A,    KC.R,    KC.S,    KC.T,    KC.G,    GITCA,          _______, KC.M,    KC.N,    KC.E,    KC.I,    KC.O,    KC.DQUO,
        SFTMOD1, KC.Z,    KC.X,    KC.C,    KC.D,    KC.V,    KC.RESET,       _______, KC.K,    KC.H,    KC.COMMA,KC.DOT,  KC.SLASH,SFTMOD2,
        KC.LCTL, GUI,     KC.LALT, KC.F12,  FN,      KC.SPC,  KC.DEL,         _______, ENTFN,   FN,      KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT
    ],
    [   # FN
        _______, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   _______,        _______, KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,
        _______, _______, _______, LCBC,    RCBC,    _______, _______,        _______, _______, _______, _______, _______, _______, KC.F12,
        _______, _______, _______, KC.LPRN, KC.RPRN, _______, _______,        _______, KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT,_______, _______,
        _______, _______, _______, KC.LBRC, KC.RBRC, _______, _______,        _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, _______,        _______, _______, _______, KC.MPLY, KC.VOLD, KC.VOLU, NXTPRV,
    ],
    [   # GUI
        _______, _______, _______, _______, _______, _______, _______,        _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, FILES,   _______, _______, SLEEP,          _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, _______,        _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, CLOSE,   _______, _______, _______,        _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, _______,        _______, _______, _______, _______, _______, _______, _______,
    ],
    [   # GAMING
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,  KC.N5,    KC.N6,          GAMING,  KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   _______,
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,   KC.T,     KC.H,           KC.RBRC, KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    _______,
        KC.BSPC, KC.A,    KC.S,    KC.D,    KC.F,   KC.G,     KC.M,           _______, KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, _______,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,   KC.B,     _______,        _______, KC.N,    KC.M,    KC.COMMA,KC.DOT,  KC.SLASH,_______,
        _______, _______, _______, _______, _______, _______, _______,        _______, _______, _______, _______, _______, _______, _______,
    ],
     [   # COLEMAK-DH SHIFTED
        S(KC.GRV), KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5, F5RUN,          GAMING,  KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.BSLS,
        S(KC.TAB), S(KC.Q),S(KC.W),S(KC.F), S(KC.P), S(KC.B), S(KC.F12),      _______, S(KC.J), S(KC.L), S(KC.U), S(KC.Y), S(KC.SCLN),S(KC.EQUAL),
        S(KC.BSPC),S(KC.A),S(KC.R),S(KC.S), S(KC.T), S(KC.G), GITCA,          _______, S(KC.M), S(KC.N), S(KC.E), S(KC.I), S(KC.O), KC.QUOT,
        _______,  S(KC.Z), S(KC.X), S(KC.C), S(KC.D), S(KC.V), KC.RESET,      _______, S(KC.K), S(KC.H), S(KC.COMMA),S(KC.DOT),S(KC.SLASH),KC.MINUS,
        S(KC.LCTL),GUI,   S(KC.LALT),S(KC.F12),FN,   S(KC.SPC),S(KC.DEL),     _______, ENTFN,   FN,      S(KC.LEFT),S(KC.DOWN),S(KC.UP),S(KC.RIGHT)
    ],
]