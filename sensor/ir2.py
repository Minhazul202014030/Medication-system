import RPi.GPIO as GPIO
import time
import webbrowser

sensor = 40
# led = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN)
# GPIO.setup(led, GPIO.OUT)
ip='http://192.168.0.104'
try:
    while True:
        if GPIO.input(sensor):
            # GPIO.output(led, False)  # LED turned on

            while GPIO.input(sensor):
                time.sleep(0.2)

            # Object detected, open the webpage
            webbrowser.open('http://127.0.0.1:8000/show_medicine40/')

            # You can customize the URL based on your requirements

        # else:
            # GPIO.output(led, True)  # LED turned off if there is no input on sensor

except KeyboardInterrupt:
    GPIO.cleanup()
