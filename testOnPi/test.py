from neopixel import *
import time
import argparse

LED_COUNT = 16  # Number of LED pixels.
LED_PIN = 19  # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN        = 10   # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 30  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 1  # set to '1' for GPIOs 13, 19, 41, 45 or 53

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def changeRainbowColor(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, wheel(i) & 255)
    strip.show()


def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def turnOffStrip(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()

def turnOnPlayer(strip, billsAddresses, color):
    for i in billsAddresses:
        #nned to test put into Color((0, 255, 255)) like this
        strip.setPixelColor(i, color)
    strip.show()

def turnOffPlayer(strip, billsAddresses):
    for i in billsAddresses:
        #nned to test put into Color((0, 255, 255)) like this
        strip.setPixelColor(i, Color(0,0,0))
    strip.show()

def setNewPlayerPosition(strip, billsAddress, newPosition, color):
    turnOffPlayer(strip, billsAddress)
    strip.setPixelColor(newPosition, color)
    strip.show()

def goByStep(strip, billsAddress, oldPos, newPos, color):
    while oldPos!=newPos:
        strip.setPixelColor(billsAddress[oldPos], Color(0,0,0))
        oldPos+=1
        strip.setPixelColor(billsAddress[oldPos], color)
        strip.show()
        time.sleep(1.0)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    billsAddress=[0, 1, 2, 3, 4, 5, 6]
    billsAddress1=[7, 8, 9, 10]
    billsAddress2=[11, 12, 13]
    billsAddress3=[7, 8, 9, 10, 11, 12, 13]

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

   # try:

        #while True:
    print('Rainbow animations.')
            #rainbow(strip)
            #rainbowCycle(strip)
            #theaterChaseRainbow(strip)
            #turnOffStrip(strip)
    #turnOnPlayer(strip, billsAddress, Color(0, 255, 0))
    #turnOnPlayer(strip, billsAddress1, Color(30, 255, 0))
    #turnOnPlayer(strip, billsAddress2, Color(0, 0, 255))
    #time.sleep(0.5)
    #turnOffPlayer(strip, billsAddress1)
    #strip.setPixelColor(0, Color(255, 0, 0))
    #strip.setPixelColor(1, Color(0, 0, 255))
    #strip.setPixelColor(2, Color(30, 255, 0))
    #strip.setPixelColor(3, Color(0, 255, 0))
    strip.setPixelColor(7, Color(0, 255, 0))
    strip.show()
    goByStep(strip, billsAddress3, 0, 6, Color(0, 255, 0))
    #time.sleep(5)
    #setNewPlayerPosition(strip, billsAddress, 9, Color(0,255,0))
    #turnOffStrip(strip)
    print("end")
    #except KeyboardInterrupt:
    #    if args.clear:
    #        colorWipe(strip, Color(0, 0, 0), 10)