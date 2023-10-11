from machine import Pin, SoftI2C
import ssd1306


i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)  # Adjust the dimensions as needed

# Clear the OLED display
oled.fill(0)
oled.show()

# Display some text
oled.text("Hello, MicroPython", 0, 0)
oled.text("on ESP32!", 0, 20)
oled.show()
