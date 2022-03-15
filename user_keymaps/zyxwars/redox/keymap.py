from kmk.keys import KC
from kmk.handlers.sequences import send_string, simple_key_sequence

_______ = KC.TRNS
LCBC = KC.LSFT(KC.LBRC)
RCBC = KC.LSFT(KC.RBRC)

# Layers
GUI = KC.LM(2, KC.LGUI)
FN = KC.MO(1)
ENTFN = KC.LT(1, KC.ENT, prefer_hold=True, tap_interrupted=False)
GAMING = KC.TG(3)

# Multi
SFTMNS = KC.MT(KC.MINUS, KC.RSFT)
SFTESC = KC.MT(KC.ESC, KC.LSFT)
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

# Home row mods
# hrm_time = 150
# A = KC.MT(KC.A, KC.LGUI, prefer_hold=False, tap_time=200, tap_interrupted=False)
# R = KC.MT(KC.R, KC.LALT, prefer_hold=False, tap_time=hrm_time, tap_interrupted=False)
# S = KC.MT(KC.S, KC.LSFT, prefer_hold=False, tap_time=hrm_time, tap_interrupted=False)
# T = KC.MT(KC.T, KC.LCTL, prefer_hold=False, tap_time=hrm_time, tap_interrupted=False)
# N = KC.MT(KC.N, KC.RCTL, prefer_hold=False, tap_time=hrm_time, tap_interrupted=False)
# E = KC.MT(KC.E, KC.RSFT, prefer_hold=False, tap_time=hrm_time, tap_interrupted=False)
# I = KC.MT(KC.I, KC.RALT, prefer_hold=False, tap_time=hrm_time, tap_interrupted=False)
# O = KC.MT(KC.O, KC.RGUI, prefer_hold=False, tap_time=200, tap_interrupted=False)

keymap = [
    #[   # QWERTY
    #    KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,  KC.N5,  F5RUN,          GAMING,  KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINUS,
    #    KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,   KC.T,   KC.LBRC,        KC.RBRC, KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.EQUAL,
    #    KC.BSPC, KC.A,    KC.S,    KC.D,    KC.F,   KC.G,   GITCA,          _______, KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,
    #    SFTESC,  KC.Z,    KC.X,    KC.C,    KC.V,   KC.B,   KC.RESET,       _______, KC.N,    KC.M,    KC.COMMA,KC.DOT,  KC.SLASH,SFTBSLS,
    #    KC.LCTL, GUI,     KC.LALT, KC.F12,  FN,     KC.SPC, KC.DEL,         ENTFN,   ENTFN,   FN,      KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT
    #],
    [   # COLEMAK-DH
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   F5RUN,          GAMING,  KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.BSLS,
        KC.TAB,  KC.Q,    KC.W,    KC.F,    KC.P,    KC.B,    KC.F12,         _______, KC.J,    KC.L,    KC.U,    KC.Y,    KC.SCLN, KC.EQUAL,
        KC.BSPC, KC.A,    KC.R,    KC.S,    KC.T,    KC.G,    GITCA,          _______, KC.M,    KC.N,    KC.E,    KC.I,    KC.O,    KC.QUOT,
        SFTESC,  KC.Z,    KC.X,    KC.C,    KC.D,    KC.V,    KC.RESET,       _______, KC.K,    KC.H,    KC.COMMA,KC.DOT,  KC.SLASH,SFTMNS,
        KC.LCTL, GUI,     KC.LALT, KC.F12,  FN,      KC.SPC,  KC.DEL,         ENTFN,   ENTFN,   FN,      KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT
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
        KC.ESC,  _______, _______, _______, _______, _______, KC.N6,          GAMING,  _______, _______, _______, _______, _______, _______,
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,   KC.T,     KC.H,           KC.RBRC, KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    _______,
        KC.BSPC, KC.A,    KC.S,    KC.D,    KC.F,   KC.G,     KC.M,           _______, KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, _______,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,   KC.B,     _______,        _______, KC.N,    KC.M,    KC.COMMA,KC.DOT,  KC.SLASH,_______,
        _______, _______, _______, _______, _______, _______, _______,        _______, _______, _______, _______, _______, _______, _______,
    ],
]

