import kmk.matrix  # isort:skip

# Thanks for sticking around. Now let's do real work, starting below

import busio
import gc

from kmk.internal_state_slave import InternalState
from kmk.matrix import MatrixScanner


class Firmware:
    debug_enabled = False

    row_pins = None
    col_pins = None
    diode_orientation = None

    extra_data_pin = None
    split_offsets = ()
    split_flip = False
    split_side = None
    split_type = None
    split_master_left = True
    is_master = False
    uart = None
    uart_flip = True
    uart_pin = None

    def __init__(self):
        self._state = InternalState(self)

    def _handle_matrix_report(self, update=None):
        '''
        Bulk processing of update code for each cycle
        :param update:
        '''
        if update is not None:
            self._state.matrix_changed(
                update[0],
                update[1],
                update[2],
            )

    def _send_to_master(self, update):
        if self.split_master_left:
            update[1] += self.split_offsets[update[0]]
        else:
            update[1] -= self.split_offsets[update[0]]
        if self.uart is not None:
            self.uart.write(update)

    def _send_debug(self, message):
        '''
        Prepends DEB and appends a newline to allow debug messages to
        be detected and handled differently than typical keypresses.
        :param message: Debug message
        '''
        if self.uart is not None:
            self.uart.write('DEB')
            self.uart.write(message, '\n')

    def init_uart(self, pin, timeout=20):
        return busio.UART(tx=pin, rx=None, timeout=timeout)

    def go(self):
        assert self.row_pins, 'no GPIO pins defined for matrix rows'
        assert self.col_pins, 'no GPIO pins defined for matrix columns'
        assert self.diode_orientation is not None, 'diode orientation must be defined'

        if self.split_flip:
            self.col_pins = list(reversed(self.col_pins))

        # Split keyboard Init
        if self.split_side == "Left":
                self.split_master_left = True
        elif self.split_side == "Right":
            self.split_master_left = False

        if self.uart_pin is not None:
            self.uart = self.init_uart(self.uart_pin)

        self.matrix = MatrixScanner(
            cols=self.col_pins,
            rows=self.row_pins,
            diode_orientation=self.diode_orientation,
            rollover_cols_every_rows=getattr(self, 'rollover_cols_every_rows', None),
            swap_indicies=getattr(self, 'swap_indicies', None),
        )

        if self.debug_enabled:
            print("Firin' lazers. Keyboard is booted.")

        while True:
            state_changed = False

            update = self.matrix.scan_for_changes()

            if update is not None:
                # This keyboard is a slave, and needs to send data to master
                self._send_to_master(update)


            if self.debug_enabled and state_changed:
                print('New State: {}'.format(self._state._to_dict()))

            gc.collect()
