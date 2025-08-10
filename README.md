# Raspberry Pi Pico WH IoT Weather Station

This project uses a Raspberry Pi Pico WH microcontroller connected to a DHT11 temperature and humidity sensor and a set of LEDs to create a simple weather station that sends data wirelessly to Adafruit IO, a cloud platform for IoT data visualization and logging.

## Project Overview

- The **DHT11 sensor** measures temperature and humidity.
- The **Pico WH** connects to a Wi-Fi network to send sensor readings to Adafruit IO.
- The device uses **LED animations** to indicate status (e.g., loading or activity).
- The code is organized into separate modules for better maintainability, including Wi-Fi connection, sensor reading, LED control, and Adafruit IO communication.
- Sensor data is sent regularly (every 10 seconds) to specific feeds on Adafruit IO, allowing remote monitoring of the environmental conditions.

## Hardware Components

- Raspberry Pi Pico WH (with built-in Wi-Fi)  
- DHT11 temperature and humidity sensor  
- 3 LEDs with appropriate resistors for visual feedback  
- Breadboard and jumper wires for connections  
- USB cable for power and programming  

## How It Works

1. On startup, the Pico connects to the specified Wi-Fi network using credentials stored securely in a separate file.
2. The DHT11 sensor is read to gather current temperature and humidity data.
3. LEDs run a simple loading animation while sensor readings and data transmission occur.
4. Sensor data is posted to Adafruit IO feeds via HTTP requests using the Pico’s Wi-Fi connection.
5. This cycle repeats indefinitely, updating the cloud dashboard regularly.

## Use Cases

- Home or office environment monitoring  
- Educational IoT demonstrations  
- Basis for expanding into more complex sensor networks or automation  

## Troubleshooting Tips

- Make sure the Wi-Fi credentials are correct and the network is 2.4 GHz compatible.  
- Ensure the DHT11 sensor wiring is correct.
- Verify LEDs are connected with correct polarity and resistors to prevent damage.  
- Check all connections on the breadboard to avoid shorts or loose wiring.

---

This project serves as a simple but practical example of integrating sensors, Wi-Fi connectivity, and cloud services on the Raspberry Pi Pico WH using MicroPython.
