import neopixel

import time
from math import e, exp, pi, sin

from kmk.extensions import Extension
from kmk.handlers.stock import passthrough as handler_passthrough
from kmk.keys import make_key
from kmk.kmktime import ticks_ms
from kmk.lib import rgb_helper

rgb_config = {}


class AnimationModes:
    OFF = 0
    STATIC = 1
    STATIC_STANDBY = 2
    BREATHING = 3
    RAINBOW = 4
    BREATHING_RAINBOW = 5
    KNIGHT = 6
    SWIRL = 7
    USER = 8


class RGB(Extension):
    pos = 0
    time = int(time.monotonic() * 10)
    intervals = (30, 20, 10, 5)

    def __init__(
        self,
        pixel_pin,
        num_pixels=0,
        val_limit=100,
        hue_default=0,
        sat_default=100,
        rgb_order=(1, 0, 2),  # GRB WS2812
        val_default=100,
        hue_step=5,
        sat_step=5,
        val_step=5,
        animation_speed=1,
        breathe_center=1,  # 1.0-2.7
        knight_effect_length=3,
        animation_mode=AnimationModes.STATIC,
        effect_init=False,
        reverse_animation=False,
        user_animation=None,
        disable_auto_write=False,
        loopcounter=0,
    ):
        self.neopixel = neopixel.NeoPixel(
            pixel_pin,
            num_pixels,
            pixel_order=rgb_order,
            auto_write=not disable_auto_write,
        )

        self.rgbw = bool(len(rgb_order) == 4)

        self.num_pixels = num_pixels
        self.hue_step = hue_step
        self.sat_step = sat_step
        self.val_step = val_step
        self.hue = hue_default
        self.hue_default = hue_default
        self.sat = sat_default
        self.sat_default = sat_default
        self.val = val_default
        self.val_default = val_default
        self.breathe_center = breathe_center
        self.knight_effect_length = knight_effect_length
        self.val_limit = val_limit
        self.animation_mode = animation_mode
        self.animation_speed = animation_speed
        self.effect_init = effect_init
        self.reverse_animation = reverse_animation
        self.user_animation = user_animation
        self.disable_auto_write = disable_auto_write
        self.loopcounter = loopcounter

        make_key(
            names=('RGB_TOG',), on_press=self._rgb_tog, on_release=handler_passthrough
        )
        make_key(
            names=('RGB_HUI',), on_press=self._rgb_hui, on_release=handler_passthrough
        )
        make_key(
            names=('RGB_HUD',), on_press=self._rgb_hud, on_release=handler_passthrough
        )
        make_key(
            names=('RGB_SAI',), on_press=self._rgb_sai, on_release=handler_passthrough
        )
        make_key(
            names=('RGB_SAD',), on_press=self._rgb_sad, on_release=handler_passthrough
        )
        make_key(
            names=('RGB_VAI',), on_press=self._rgb_vai, on_release=handler_passthrough
        )
        make_key(
            names=('RGB_VAD',), on_press=self._rgb_vad, on_release=handler_passthrough
        )
        make_key(
            names=('RGB_ANI',), on_press=self._rgb_ani, on_release=handler_passthrough
        )
        make_key(
            names=('RGB_AND',), on_press=self._rgb_and, on_release=handler_passthrough
        )
        make_key(
            names=('RGB_MODE_PLAIN', 'RGB_M_P'),
            on_press=self._rgb_mode_static,
            on_release=handler_passthrough,
        )
        make_key(
            names=('RGB_MODE_BREATHE', 'RGB_M_B'),
            on_press=self._rgb_mode_breathe,
            on_release=handler_passthrough,
        )
        make_key(
            names=('RGB_MODE_RAINBOW', 'RGB_M_R'),
            on_press=self._rgb_mode_rainbow,
            on_release=handler_passthrough,
        )
        make_key(
            names=('RGB_MODE_BREATHE_RAINBOW', 'RGB_M_BR'),
            on_press=self._rgb_mode_breathe_rainbow,
            on_release=handler_passthrough,
        )
        make_key(
            names=('RGB_MODE_SWIRL', 'RGB_M_S'),
            on_press=self._rgb_mode_swirl,
            on_release=handler_passthrough,
        )
        make_key(
            names=('RGB_MODE_KNIGHT', 'RGB_M_K'),
            on_press=self._rgb_mode_knight,
            on_release=handler_passthrough,
        )
        make_key(
            names=('RGB_RESET', 'RGB_RST'),
            on_press=self._rgb_reset,
            on_release=handler_passthrough,
        )

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, sandbox):
        return

    def before_matrix_scan(self, sandbox):
        return

    def after_matrix_scan(self, sandbox):
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        self.animate()

    def on_powersave_enable(self, sandbox):
        return

    def on_powersave_disable(self, sandbox):
        self._do_update()

    def _rgb_hui(self, *args, **kwargs):
        rgb_helper.increase_hue(self)

    def _rgb_hud(self, *args, **kwargs):
        rgb_helper.decrease_hue(self)

    def _rgb_sai(self, *args, **kwargs):
        rgb_helper.increase_sat(self)

    def _rgb_sad(self, *args, **kwargs):
        rgb_helper.decrease_sat(self)

    def _rgb_vai(self, *args, **kwargs):
        rgb_helper.increase_val(self)

    def _rgb_vad(self, *args, **kwargs):
        rgb_helper.decrease_val(self)

    def _rgb_ani(self, *args, **kwargs):
        rgb_helper.increase_ani(self)

    def _rgb_and(self, *args, **kwargs):
        rgb_helper.decrease_ani(self)

    def _rgb_mode_static(self, *args, **kwargs):
        self.effect_init = True
        self.animation_mode = AnimationModes.STATIC

    def _rgb_mode_breathe(self, *args, **kwargs):
        self.effect_init = True
        self.animation_mode = AnimationModes.BREATHING

    def _rgb_mode_breathe_rainbow(self, *args, **kwargs):
        self.effect_init = True
        self.animation_mode = AnimationModes.BREATHING_RAINBOW

    def _rgb_mode_rainbow(self, *args, **kwargs):
        self.effect_init = True
        self.animation_mode = AnimationModes.RAINBOW

    def _rgb_mode_swirl(self, *args, **kwargs):
        self.effect_init = True
        self.animation_mode = AnimationModes.SWIRL

    def _rgb_mode_knight(self, *args, **kwargs):
        self.effect_init = True
        self.animation_mode = AnimationModes.KNIGHT

    def _rgb_reset(self, *args, **kwargs):
        self.hue = self.hue_default
        self.sat = self.sat_default
        self.val = self.val_default
        if self.animation_mode == AnimationModes.STATIC_STANDBY:
            self.animation_mode = AnimationModes.STATIC
        self._do_update()

    def animate(self):
        '''
        Activates a "step" in the animation based on the active mode
        :return: Returns the new state in animation
        '''
        if self.effect_init:
            self._init_effect()

        if self.animation_mode is not AnimationModes.STATIC_STANDBY:
            self.loopcounter += 1
            if self.loopcounter >= 7 and self.enable:
                self.loopcounter = 0
                if self.animation_mode == AnimationModes.BREATHING:
                    self.effect_breathing()
                elif self.animation_mode == AnimationModes.RAINBOW:
                    self.effect_rainbow()
                elif self.animation_mode == AnimationModes.BREATHING_RAINBOW:
                    self.effect_breathing_rainbow()
                elif self.animation_mode == AnimationModes.STATIC:
                    self.effect_static()
                elif self.animation_mode == AnimationModes.KNIGHT:
                    self.effect_knight()
                elif self.animation_mode == AnimationModes.SWIRL:
                    self.effect_swirl()
                elif self.animation_mode == AnimationModes.USER:
                    self.user_animation(self)
                elif self.animation_mode == AnimationModes.STATIC_STANDBY:
                    pass
                else:
                    rgb_helper.off(self)
                if self.loopcounter >= 7:
                    self.loopcounter = 0

    def _animation_step(self):
        interval = ticks_ms() - self.time
        if interval >= max(self.intervals):
            self.time = ticks_ms()
            return max(self.intervals)
        if interval in self.intervals:
            return interval
        return None

    def _init_effect(self):
        if (
            self.animation_mode == AnimationModes.BREATHING
            or self.animation_mode == AnimationModes.BREATHING_RAINBOW
        ):
            self.intervals = (30, 20, 10, 5)
        elif self.animation_mode == AnimationModes.SWIRL:
            self.intervals = (50, 50)

        self.pos = 0
        self.reverse_animation = False
        self.effect_init = False

    def _check_update(self):
        return bool(self.animation_mode == AnimationModes.STATIC_STANDBY)

    def _do_update(self):
        if self.animation_mode == AnimationModes.STATIC_STANDBY:
            self.animation_mode = AnimationModes.STATIC

    def effect_static(self):
        rgb_helper.set_hsv_fill(self, self.hue, self.sat, self.val)
        self.animation_mode = AnimationModes.STATIC_STANDBY

    def effect_breathing(self):
        # http://sean.voisen.org/blog/2011/10/breathing-led-with-arduino/
        # https://github.com/qmk/qmk_firmware/blob/9f1d781fcb7129a07e671a46461e501e3f1ae59d/quantum/rgblight.c#L806
        sined = sin((self.pos / 255.0) * pi)
        multip_1 = exp(sined) - self.breathe_center / e
        multip_2 = self.val_limit / (e - 1 / e)

        self.val = int(multip_1 * multip_2)
        self.pos = (self.pos + self.animation_speed) % 256
        rgb_helper.set_hsv_fill(self, self.hue, self.sat, self.val)

    def effect_breathing_rainbow(self):
        rgb_helper.increase_hue(self, self.animation_speed)
        self.effect_breathing()

    def effect_rainbow(self):
        rgb_helper.increase_hue(self, self.animation_speed)
        rgb_helper.set_hsv_fill(self, self.hue, self.sat, self.val)

    def effect_swirl(self):
        rgb_helper.increase_hue(self, self.animation_speed)
        self.disable_auto_write = True  # Turn off instantly showing
        for i in range(0, self.num_pixels):
            rgb_helper.set_hsv(
                self, (self.hue - (i * self.num_pixels)) % 360, self.sat, self.val, i
            )

        # Show final results
        self.disable_auto_write = False  # Resume showing changes
        rgb_helper.show(self)

    def effect_knight(self):
        # Determine which LEDs should be lit up
        self.disable_auto_write = True  # Turn off instantly showing
        rgb_helper.off(self)  # Fill all off
        pos = int(self.pos)

        # Set all pixels on in range of animation length offset by position
        for i in range(pos, (pos + self.knight_effect_length)):
            rgb_helper.set_hsv(self, self.hue, self.sat, self.val, i)

        # Reverse animation when a boundary is hit
        if pos >= self.num_pixels or pos - 1 < (self.knight_effect_length * -1):
            self.reverse_animation = not self.reverse_animation

        if self.reverse_animation:
            self.pos -= self.animation_speed / 2
        else:
            self.pos += self.animation_speed / 2

        # Show final results
        self.disable_auto_write = False  # Resume showing changes
        rgb_helper.show(self)

    def _rgb_tog(self, *args, **kwargs):
        if self.animation_mode == AnimationModes.STATIC:
            self.animation_mode = AnimationModes.STATIC_STANDBY
            self._do_update()
        if self.animation_mode == AnimationModes.STATIC_STANDBY:
            self.animation_mode = AnimationModes.STATIC
            self._do_update()
        if self.enable:
            rgb_helper.off(self)
        self.enable = not self.enable
