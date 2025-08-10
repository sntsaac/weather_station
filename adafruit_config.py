import urequests
import secrets

BASE_URL = "https://io.adafruit.com/api/v2/{}/feeds/{}/data"

def send_data(feed_name, value):
    url = BASE_URL.format(secrets.ADAFRUIT_IO_USERNAME, feed_name)
    headers = {"X-AIO-Key": secrets.ADAFRUIT_IO_KEY, "Content-Type": "application/json"}
    data = '{"value": ' + str(value) + '}'

    try:
        response = urequests.post(url, headers=headers, data=data)
        response.close()
        print(f"Sent {value} to {feed_name}")
    except Exception as e:
        print("Error sending data:", e)
