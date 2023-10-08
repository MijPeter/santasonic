import array, time
from machine import Pin
import rp2


@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1).side(0)[T3 - 1]
    jmp(not_x, "do_zero").side(1)[T1 - 1]
    jmp("bitloop").side(1)[T2 - 1]
    label("do_zero")
    nop().side(0)[T2 - 1]
    wrap()


class AddressedRGBLed:
    def __init__(self, num_leds, pin):
        self.num_leds = num_leds
        self.color_arr = array.array("I", [0 for _ in range(self.num_leds)])
        self.state_machine = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(pin))
        self.state_machine.active(1)

    def set(self, color=(0, 0, 0), brightness=0.07, pos=None):
        if pos is None:
            for i in range(self.num_leds):
                self._set_pixel(i, color, brightness)
        else:
            self._set_pixel(pos, color, brightness)

        self._show()

    def _set_pixel(self, i, color, brightness):
        self.color_arr[i] = ((int(color[0] * brightness)) << 16) + ((int(color[1] * brightness)) << 8) + int(
            color[2] * brightness)

    def _show(self):
        self.state_machine.put(self.color_arr, 8)
        time.sleep_ms(10)

    # You can also add other utility functions like color_chase, rainbow_cycle, etc.
