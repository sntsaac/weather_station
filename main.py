import time
import dht
from machine import Pin
import wifi_connect
import adafruit_io
import leds

# Setup sensor
dht_sensor = dht.DHT11(Pin(28))

# Connect to WiFi
wifi_connect.connect_wifi()

while True:
    leds.loading_animation()

    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()

        print(f"Temperature: {temp}°C, Humidity: {hum}%")

        # Send to Adafruit IO
        adafruit_io.send_data("temperature", temp)
        adafruit_io.send_data("humidity", hum)

    except Exception as e:
        print("Error reading sensor:", e)

    leds.all_off()
    time.sleep(10)  # wait before next reading
