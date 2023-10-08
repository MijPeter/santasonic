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
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()

class AddressedRGBLed:
    def __init__(self, led_num, pin, default_brightness=1.0):
        self.NUM_LEDS = led_num
        self.brightness = default_brightness
        self.ar = array.array("I", [0 for _ in range(self.NUM_LEDS)])
        self.sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(pin))
        self.sm.active(1)

    def show(self):
        dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
        for i,c in enumerate(ar):
            r = int(((c >> 8) & 0xFF) * self.brightness)
            g = int(((c >> 16) & 0xFF) * self.brightness)
            b = int((c & 0xFF) * self.brightness)
            dimmer_ar[i] = (g<<16) + (r<<8) + b
        sm.put(dimmer_ar, 8)
        time.sleep_ms(10)


    def set(self, pos=None, color=(0, 0, 0), brightness=None):
        if brightness:
            self.brightness = brightness

        if pos is None:
            for i in range(self.NUM_LEDS):
                self._set_pixel(i, color)
        else:
            self._set_pixel(pos, color)

    def _set_pixel(self, i, color):
        self.ar[i] = (color[1] << 16) + (color[0] << 8) + color[2]

    # You can also add other utility functions like color_chase, rainbow_cycle, etc.
