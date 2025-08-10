from machine import Pin
import time

led_pins = [Pin(2, Pin.OUT), Pin(3, Pin.OUT), Pin(4, Pin.OUT)]

def loading_animation():
    for _ in range(2):  # repeat twice
        for led in led_pins:
            led.on()
            time.sleep(0.2)
            led.off()
    time.sleep(0.5)

def all_off():
    for led in led_pins:
        led.off()
