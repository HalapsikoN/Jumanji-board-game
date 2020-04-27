#from neopixel import *
import time
import logging
import random

# LED strip configuration:
LED_COUNT = 16          # Number of LED pixels.
LED_PIN = 26            # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN        = 10   # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000    # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10            # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100    # Set to 0 for darkest and 255 for brightest
LED_INVERT = False      # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 1         # set to '1' for GPIOs 13, 19, 41, 45 or 53


def ledWork(queue, event):
    #strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    #strip.begin()
    counter=0
    while not event.is_set():
        if not queue.empty():
            counter=queue.get()
        print(random.randrange(1, 7))
        counter+=1
        time.sleep(1.0)

    print("gg")
