def hsv_to_rgb(rgb_obj, hue, sat, val):
    '''
    Converts HSV values, and returns a tuple of RGB values
    :param hue:
    :param sat:
    :param val:
    :return: (r, g, b)
    '''
    r = 0
    g = 0
    b = 0

    if val > rgb_obj.val_limit:
        val = rgb_obj.val_limit

    if sat == 0:
        r = val
        g = val
        b = val

    else:
        base = ((100 - sat) * val) / 100
        color = (val - base) * ((hue % 60) / 60)

        x = int(hue / 60)
        if x == 0:
            r = val
            g = base + color
            b = base
        elif x == 1:
            r = val - color
            g = val
            b = base
        elif x == 2:
            r = base
            g = val
            b = base + color
        elif x == 3:
            r = base
            g = val - color
            b = val
        elif x == 4:
            r = base + color
            g = base
            b = val
        elif x == 5:
            r = val
            g = base
            b = val - color

    return int(r), int(g), int(b)


def hsv_to_rgbw(rgb_obj, hue, sat, val):
    '''
    Converts HSV values, and returns a tuple of RGBW values
    :param hue:
    :param sat:
    :param val:
    :return: (r, g, b, w)
    '''
    rgb = rgb_obj.hsv_to_rgb(hue, sat, val)
    return rgb[0], rgb[1], rgb[2], min(rgb)


def set_hsv(rgb_obj, hue, sat, val, index):
    '''
    Takes HSV values and displays it on a single LED/Neopixel
    :param hue:
    :param sat:
    :param val:
    :param index: Index of LED/Pixel
    '''
    if rgb_obj.neopixel:
        if rgb_obj.rgbw:
            rgb_obj.set_rgb(rgb_obj.hsv_to_rgbw(hue, sat, val), index)
        else:
            rgb_obj.set_rgb(rgb_obj.hsv_to_rgb(hue, sat, val), index)


def set_hsv_fill(rgb_obj, hue, sat, val):
    '''
    Takes HSV values and displays it on all LEDs/Neopixels
    :param hue:
    :param sat:
    :param val:
    '''
    if rgb_obj.neopixel:
        if rgb_obj.rgbw:
            rgb_obj.set_rgb_fill(rgb_obj.hsv_to_rgbw(hue, sat, val))
        else:
            rgb_obj.set_rgb_fill(rgb_obj.hsv_to_rgb(hue, sat, val))


def set_rgb(rgb_obj, rgb, index):
    '''
    Takes an RGB or RGBW and displays it on a single LED/Neopixel
    :param rgb: RGB or RGBW
    :param index: Index of LED/Pixel
    '''
    if rgb_obj.neopixel and 0 <= index <= rgb_obj.num_pixels - 1:
        rgb_obj.neopixel[index] = rgb
        if not rgb_obj.disable_auto_write:
            rgb_obj.neopixel.show()


def set_rgb_fill(rgb_obj, rgb):
    '''
    Takes an RGB or RGBW and displays it on all LEDs/Neopixels
    :param rgb: RGB or RGBW
    '''
    if rgb_obj.neopixel:
        rgb_obj.neopixel.fill(rgb)
        if not rgb_obj.disable_auto_write:
            rgb_obj.neopixel.show()


def increase_hue(rgb_obj, step=None):
    '''
    Increases hue by step amount rolling at 360 and returning to 0
    :param step:
    '''
    if not step:
        step = rgb_obj.hue_step

    rgb_obj.hue = (rgb_obj.hue + step) % 360

    if rgb_obj._check_update():
        rgb_obj._do_update()


def decrease_hue(rgb_obj, step=None):
    '''
    Decreases hue by step amount rolling at 0 and returning to 360
    :param step:
    '''
    if not step:
        step = rgb_obj.hue_step

    if (rgb_obj.hue - step) <= 0:
        rgb_obj.hue = (rgb_obj.hue + 360 - step) % 360
    else:
        rgb_obj.hue = (rgb_obj.hue - step) % 360

    if rgb_obj._check_update():
        rgb_obj._do_update()


def increase_sat(rgb_obj, step=None):
    '''
    Increases saturation by step amount stopping at 100
    :param step:
    '''
    if not step:
        step = rgb_obj.sat_step

    if rgb_obj.sat + step >= 100:
        rgb_obj.sat = 100
    else:
        rgb_obj.sat += step

    if rgb_obj._check_update():
        rgb_obj._do_update()


def decrease_sat(rgb_obj, step=None):
    '''
    Decreases saturation by step amount stopping at 0
    :param step:
    '''
    if not step:
        step = rgb_obj.sat_step

    if (rgb_obj.sat - step) <= 0:
        rgb_obj.sat = 0
    else:
        rgb_obj.sat -= step

    if rgb_obj._check_update():
        rgb_obj._do_update()


def increase_val(rgb_obj, step=None):
    '''
    Increases value by step amount stopping at 100
    :param step:
    '''
    if not step:
        step = rgb_obj.val_step
    if (rgb_obj.val + step) >= 100:
        rgb_obj.val = 100
    else:
        rgb_obj.val += step

    if rgb_obj._check_update():
        rgb_obj._do_update()


def decrease_val(rgb_obj, step=None):
    '''
    Decreases value by step amount stopping at 0
    :param step:
    '''
    if not step:
        step = rgb_obj.val_step
    if (rgb_obj.val - step) <= 0:
        rgb_obj.val = 0
    else:
        rgb_obj.val -= step

    if rgb_obj._check_update():
        rgb_obj._do_update()


def increase_ani(rgb_obj):
    '''
    Increases animation speed by 1 amount stopping at 10
    :param step:
    '''
    if (rgb_obj.animation_speed + 1) > 10:
        rgb_obj.animation_speed = 10
    else:
        rgb_obj.animation_speed += 1
    if rgb_obj._check_update():
        rgb_obj._do_update()


def decrease_ani(rgb_obj):
    '''
    Decreases animation speed by 1 amount stopping at 0
    :param step:
    '''
    if (rgb_obj.animation_speed - 1) <= 0:
        rgb_obj.animation_speed = 0
    else:
        rgb_obj.animation_speed -= 1
    if rgb_obj._check_update():
        rgb_obj._do_update()


def off(rgb_obj):
    '''
    Turns off all LEDs/Neopixels without changing stored values
    '''
    if rgb_obj.neopixel:
        rgb_obj.set_hsv_fill(0, 0, 0)


def show(rgb_obj):
    '''
    Turns on all LEDs/Neopixels without changing stored values
    '''
    if rgb_obj.neopixel:
        rgb_obj.neopixel.show()
