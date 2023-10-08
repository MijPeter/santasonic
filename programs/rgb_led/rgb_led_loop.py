import math
import rgb_led


def rgb_from_angle(angle):
    """Convert an angle to an RGB color using sine waves."""
    red = math.sin(angle) * 127.5 + 127.5
    green = math.sin(angle + 2 * math.pi / 3) * 127.5 + 127.5
    blue = math.sin(angle + 4 * math.pi / 3) * 127.5 + 127.5

    return (int(red), int(green), int(blue))


"""Print rainbow RGB colors smoothly in a cycle."""
leds = rgb_led.AddressedRGBLed(num_leds=4, pin=22)

angles = [-360, -180, 0, 180]
step = 0.1

while True:
    for i, angle in enumerate(angles):
        color = rgb_from_angle(angle)
        leds.set(pos=i, color=color)

    for i in range(len(angles)):
        angles[i] += step
        if angles[i] > 2 * math.pi:
            angles[i] -= 2 * math.pi
