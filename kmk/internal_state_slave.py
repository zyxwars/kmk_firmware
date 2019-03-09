from kmk.util import intify_coordinate


class InternalState:
    keys_pressed = set()
    coord_keys_pressed = {}

    def __init__(self, config):
        self.config = config

    def __repr__(self):
        return 'InternalState({})'.format(self._to_dict())

    def _to_dict(self):
        ret = {
            'keys_pressed': self.keys_pressed,
        }

        return ret

    def _find_key_in_map(self, row, col):
        # Later-added layers have priority. Sift through the layers
        # in reverse order until we find a valid keycode object
        for layer in self.reversed_active_layers:
            layer_key = self.config.keymap[layer][row][col]

            if self.config.debug_enabled:
                print('Resolved key: {}'.format(layer_key))

            return layer_key

    def matrix_changed(self, row, col, is_pressed):
        if self.config.debug_enabled:
            print('Matrix changed (col, row, pressed?): {}, {}, {}'.format(
                col, row, is_pressed,
            ))

        int_coord = intify_coordinate(row, col)
        kc_changed = self._find_key_in_map(row, col)

        if kc_changed is None:
            print('No key accessible for col, row: {}, {}'.format(row, col))
            return self

        return self.process_key(kc_changed, is_pressed, int_coord, (row, col))

    def process_key(self, key, is_pressed, coord_int=None, coord_raw=None):
        if self.tapping:
            self._process_tap_dance(key, is_pressed)
        else:
            if is_pressed:
                key._on_press(self, coord_int, coord_raw)
            else:
                key._on_release(self, coord_int, coord_raw)

            if self.config.leader_mode % 2 == 1:
                self._process_leader_mode()

        return self

    def remove_key(self, keycode):
        self.keys_pressed.discard(keycode)
        return self.process_key(keycode, False)

    def add_key(self, keycode):
        self.keys_pressed.add(keycode)
        return self.process_key(keycode, True)

    def tap_key(self, keycode):
        self.add_key(keycode)
        # On the next cycle, we'll remove the key.
        self.set_timeout(False, lambda: self.remove_key(keycode))

        return self


