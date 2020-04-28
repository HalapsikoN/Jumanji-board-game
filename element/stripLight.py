# from neopixel import *
import time
import logging
import random

# LED strip configuration:
from classes.Message import *
from util.commonFunctions import readPlayersBillsAddreses
from classes.Player import Player

LED_COUNT = 16  # Number of LED pixels.
LED_PIN = 26  # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN        = 10   # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 1  # set to '1' for GPIOs 13, 19, 41, 45 or 53

# def wheel(pos):
#     """Generate rainbow colors across 0-255 positions."""
#     if pos < 85:
#         return Color(pos * 3, 255 - pos * 3, 0)
#     elif pos < 170:
#         pos -= 85
#         return Color(255 - pos * 3, 0, pos * 3)
#     else:
#         pos -= 170
#         return Color(0, pos * 3, 255 - pos * 3)
#
#
# def rainbow(strip, wait_ms=20, iterations=1):
#     """Draw rainbow that fades across all pixels at once."""
#     for j in range(256 * iterations):
#         for i in range(strip.numPixels()):
#             strip.setPixelColor(i, wheel((i + j) & 255))
#         strip.show()
#         time.sleep(wait_ms / 1000.0)
#
# def changeRainbowColor(strip):
#     for i in range(strip.numPixels()):
#         strip.setPixelColor(i, wheel(i)&255)
#     strip.show()
#
# def rainbowCycle(strip, wait_ms=20, iterations=5):
#     """Draw rainbow that uniformly distributes itself across all pixels."""
#     for j in range(256 * iterations):
#         for i in range(strip.numPixels()):
#             strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
#         strip.show()
#         time.sleep(wait_ms / 1000.0)
#
#
# def theaterChaseRainbow(strip, wait_ms=50):
#     """Rainbow movie theater light style chaser animation."""
#     for j in range(256):
#         for q in range(3):
#             for i in range(0, strip.numPixels(), 3):
#                 strip.setPixelColor(i + q, wheel((i + j) % 255))
#             strip.show()
#             time.sleep(wait_ms / 1000.0)
#             for i in range(0, strip.numPixels(), 3):
#                 strip.setPixelColor(i + q, 0)

def ledWork(queue, event):
    # strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # strip.begin()

    playersAddresses = readPlayersBillsAddreses('./text/playersBillsAddresses.txt')
    playersColors = [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 255, 0)
    ]
    print(playersAddresses)
    print(playersColors)

    player = 0
    currentCommand = START_UP_FUNCTION
    newCommand = 0

    while True:
        if not queue.empty():
            message = queue.get()
            currentCommand = message.command
            player = message.player

        if currentCommand == START_UP_FUNCTION:
            # changeRainbowColor(strip)
            print(0)

        if currentCommand == PRINT_USER:
            print(player)

        if currentCommand == EXIT:
            break

        time.sleep(1.0)
