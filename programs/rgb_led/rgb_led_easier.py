import rgb_led

leds = rgb_led.AddressedRGBLed(led_num=4, pin=22, default_brightness=0.1)
leds.set(color=(255, 0, 0))  # Sets all LEDs to red with the default brightness
leds.set(pos=0, color=(0, 255, 0))  # Sets the LED at position 0 to green with the default brightness
leds.set(pos=1, color=(0, 0, 255), brightness=0.5)  # Sets the LED at position 1 to blue with half brightness

leds.show()
