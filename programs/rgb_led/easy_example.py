import rgb_led

leds = rgb_led.AddressedRGBLed(num_leds=4, pin=22)

# set all leds to color (0, 255, 255)
leds.set(color=(0, 255, 255))

# set led at position 2 to color (0, 0, 0) (black)
leds.set(pos=2)

leds.set(pos=1, color=(255, 0, 0), brightness=0.02)
