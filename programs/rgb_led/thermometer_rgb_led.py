import machine
import rgb_led
import utime


def temperature_to_rgb(temp):
    # Check if the temperature is within the valid range
    if temp < 15:
        return (0, 0, 255)
    elif temp > 25:
        return (255, 0, 0)

    # Map the temperature between 15 and 25 to a value between 0 and 1
    normalized_temp = (temp - 15) / 10

    # Interpolate between blue and red
    red = int(255 * normalized_temp)
    green = 0
    blue = int(255 * (1 - normalized_temp))

    return (red, green, blue)


sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

rgb_leds = rgb_led.AddressedRGBLed(num_leds=4, pin=22)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)

    rgb_leds.set(temperature_to_rgb(temperature))

    utime.sleep(2)