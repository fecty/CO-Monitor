import uasyncio as asyncio
from uasyncio import sleep as asleep
from machine import Pin, SoftI2C, TouchPad, ADC
import ssd1306


async def main():
    buz = Pin(buz_pin, Pin.OUT)  # buzzer for sound

    display = ssd1306.SSD1306_I2C(oledX, oledY, i2c)  # oled display
    display.fill(0)

    touch = TouchPad(Pin(touch_pin, mode=Pin.IN))  # capacitive touch sensor

    sensor = ADC(Pin(mq7_pin))
    while True:
        await asleep(1)
        touch_value = touch.read()
        ppm = (1980/4095)*sensor.read()+20
        print(f'Carbon Monoxide Concentration: {ppm}')
        asyncio.create_task(draw(display, ppm))

        if touch_value < 500:
            print('quitting...')
            await buzz(buz, 2, .1)
            break


async def draw(display, val):
    display.fill(0)
    display.text('CO Monitor', 2, 2, 1)  # title

    display.rect(0, 0, oledX, oledY, 1)  # draw rectangle around display

    display.rect(85, 0, 43, 20, 1)  # for the value
    display.text(str(round(val)), 90, 5)

    display.line(0, 22, 128, 22, 1)

    display.show()


async def buzz(buz, n, dur):
    i = 0
    print('buzzing...')
    while i < n:
        buz.on()
        await asleep(dur)
        buz.off()
        await asleep(dur)
        i += 1

buz_pin = 32  # digital
touch_pin = 4  # touch sensor
scl_pin = 22  # I2C
sda_pin = 21  # I2C
mq7_pin = 36  # analog

oledX = 128
oledY = 64

i2c = SoftI2C(sda=Pin(sda_pin), scl=Pin(scl_pin))

asyncio.run(main())
