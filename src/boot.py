import esp
import gc
import webrepl
from time import sleep


esp.osdebug(0)
gc.enable()


def do_connect(ssid, pwd):  # connect to local network for WebRepl
    import network

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, pwd)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


def buzz(buz, n, dur):
    i = 0
    print('buzzing...')
    while i < n:
        buz.on()
        sleep(dur)
        buz.off()
        sleep(dur)
        i += 1


def main():
    from time import sleep
    from machine import SoftI2C, Pin
    import ssd1306

    print('booting...')

    print('Carbon Monoxide Monitor created by Zurain Nazir, 10th Daffodil and Shalizeh Asif, 11th Daffodil from G.D. Goenka Public School Srinagar in September 2023 for school science fair.')

    buz_pin = 32  # digital
    oledX = 128
    oledY = 64
    scl_pin = 22  # I2C
    sda_pin = 21  # I2C

    buz = Pin(buz_pin, Pin.OUT)
    buzz(buz, 2, .1)
    i2c = SoftI2C(sda=Pin(sda_pin), scl=Pin(scl_pin))
    print(f'I2C SDA: {sda_pin} SCL: {scl_pin}')
    display = ssd1306.SSD1306_I2C(oledX, oledY, i2c)  # oled display
    print('oled initiated...')

    display.fill(0)

    display.text('CO Monitor', 25, 1, 1)

    display.text('Zurain 10D', 0, 15, 1)
    display.text('Shalizeh 11D', 0, 30, 1)
    display.text('G.D. Goenka 2023', 0, 45, 1)

    display.show()

    do_connect('Home', 'ambrosia')
    # webrepl.start() # comment it out when done with project.


main()
