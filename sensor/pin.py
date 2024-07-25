import RPi.GPIO as GPIO
import time
import webbrowser

# Define GPIO pins for 5 sensors
sensors = [16,18,22,40]

GPIO.setmode(GPIO.BOARD)

# Set up GPIO pins for sensors
for sensor in sensors:
    GPIO.setup(sensor, GPIO.IN)

ip='http://192.168.0.104'

try:
    while True:
        for sensor_pin in sensors:
            if GPIO.input(sensor_pin):
                while GPIO.input(sensor_pin):
                    time.sleep(0.2)

                # Object detected, open the webpage
                webbrowser.open(f'http://127.0.0.1:8000/show_medicine{sensor_pin}/')

except KeyboardInterrupt:
    GPIO.cleanup()
