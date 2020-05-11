import random
import threading
import time

import board
import neopixel

from classes.DoubleColorPointInf import *
# LED strip configuration:
from classes.Message import *
from util.commonFunctions import readPlayersBillsAddreses

# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 124

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(pixels, wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


# turn off board
def turnOffBoard(pixels):
    pixels.fill((0, 0, 0))
    pixels.show()


# rainbow standart tainbow rownd
def standartFunction(pixels):
    rainbow_cycle(pixels, 0.006)
    pixels.show()


# plyer move in game
def playersOnOnePoint(pixels, billAddreses, position, savedColor, colorOnPoint, event):
    wait = 0.5
    while not event.is_set():
        pixels[billAddreses[position]] = savedColor
        pixels.show()
        time.sleep(wait)
        pixels[billAddreses[position]] = colorOnPoint
        pixels.show()
        time.sleep(wait)


def isPlayerOnPoint(pixels, position):
    return pixels[position] == (0, 0, 0)


def playerMove(pixels, addressList, startPosition, endPosition, step):
    color = pixels[addressList[startPosition]]
    wait = 1

    currentPosition = startPosition
    nextPosition = startPosition + step

    savedColor = 0

    while currentPosition != endPosition:
        if savedColor != 0:
            pixels[addressList[currentPosition]] = savedColor
            savedColor = 0
        else:
            pixels[addressList[currentPosition]] = (0, 0, 0)

        if nextPosition >= len(addressList) or nextPosition < 0:
            pixels.show()
            time.sleep(wait)
            break

        if pixels[addressList[nextPosition]] != (0, 0, 0):
            savedColor = pixels[addressList[nextPosition]]

        pixels[addressList[nextPosition]] = color

        currentPosition += step
        nextPosition += step
        pixels.show()
        time.sleep(wait)

    return savedColor


def playerMoveFromOnePlayerPoint(pixels, billAddresses, startAddress, endAddress, step):
    if startAddress < 0:
        startAddress = 0
    if endAddress>=len(billAddresses):
        endAddress=len(billAddresses)-1

    savedColor = playerMove(pixels, billAddresses, startAddress, endAddress, step)
    currentColor = pixels[billAddresses[endAddress]]
    if savedColor != 0:
        event = threading.Event()
        thread = threading.Thread(target=playersOnOnePoint,
                                  args=(pixels, billAddresses, endAddress, savedColor, currentColor, event))
        thread.start()
        return DoubleColorPointInf(billAddresses[endAddress], [currentColor, savedColor], thread, event)
    else:
        return 0


def playerMoveFromTwoPlayerPoint(pixels, billAddreses, startAddress, endAddress, step, playerColor,
                                 doubleColorPointInf):
    thread = doubleColorPointInf.thread
    event = doubleColorPointInf.eventToStop
    event.set()
    thread.join()

    pointColors = doubleColorPointInf.colors
    pointColors.remove(playerColor)
    savedColor = pointColors[0]

    pixels[billAddreses[startAddress]] = savedColor
    startAddress += step

    if startAddress < len(billAddreses):
        pixels[billAddreses[startAddress]] = playerColor
        pixels.show()
        time.sleep(0.5)
        return playerMoveFromOnePlayerPoint(pixels, billAddreses, startAddress, endAddress, step)
    else:
        pixels.show()
        return 0


# for option show
def showPlayers(pixels, playersAddresses, playerColors, playersInGame):
    turnOffBoard(pixels)
    for i in range(4):
        if playersInGame[i] == 1:
            showPlayer(pixels, playersAddresses[i], playerColors[i])
    pixels.show()


def showPlayer(pixels, billAddresses, color):
    for element in billAddresses:
        if pixels[element] == (0, 0, 0):
            pixels[element] = color
        else:
            pixels[element] = (255, 255, 255)


# snake
def snakeEffectFromCenter(pixels, billAddresses, color, size, wait=0.5):
    start = len(billAddresses) - 1
    end = len(billAddresses) - 1
    while end - start < size:
        pixels[billAddresses[start]] = color
        start -= 1
        time.sleep(wait)
        pixels.show()
    while end != size - 1:
        pixels[billAddresses[end]] = (0, 0, 0)
        pixels[billAddresses[start]] = color
        end -= 1
        start -= 1
        time.sleep(wait)
        pixels.show()
    while end >= 0:
        pixels[billAddresses[end]] = (0, 0, 0)
        end -= 1
        time.sleep(wait)
        pixels.show()


def snakeEffectToCenter(pixels, billAddresses, color, size, wait=0.5):
    start = 0
    end = 0
    while start < size:
        pixels[billAddresses[start]] = color
        start += 1
        time.sleep(wait)
        pixels.show()
    while start <= len(billAddresses) - 1:
        pixels[billAddresses[end]] = (0, 0, 0)
        pixels[billAddresses[start]] = color
        end += 1
        start += 1
        time.sleep(wait)
        pixels.show()
    while end <= len(billAddresses) - 1:
        pixels[billAddresses[end]] = (0, 0, 0)
        end += 1
        time.sleep(wait)
        pixels.show()


def fillAllEffectFromCenter(pixels, billAddresses, color, wait=0.5):
    maxLen = 0
    for element in billAddresses:
        if len(element) > maxLen:
            maxLen = len(element)
    for i in range(maxLen):
        for j in range(len(billAddresses)):
            if i < len(billAddresses[j]):
                pixels[billAddresses[j][i]] = color
        pixels.show()
        time.sleep(wait)


def randomColorAndWhite(pixels, color, numberColor=int(num_pixels / 3)):
    array = random.sample(range(len(pixels)), numberColor * 2)
    for i in range(numberColor):
        pixels[array[i]] = color
        pixels[array[i + numberColor]] = (255, 255, 255)
    pixels.show()


def ledWork(queue):
    pixels = neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
    )

    playersAddresses = readPlayersBillsAddreses('./text/playersBillsAddresses.txt')
    playersColors = [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 255, 0)
    ]

    data = 0
    currentCommand = START_UP_FUNCTION
    message = Message(START_UP_FUNCTION)
    doubleColorPoints = {}

    while True:
        if not queue.empty():
            message = queue.get()
            currentCommand = message.command
            data = message.data

        if currentCommand == START_UP_FUNCTION:
            print("START_UP_FUNCTION")
            standartFunction(pixels)

        if currentCommand == OPTION_CHOOSE:
            print("OPTION_CHOOSE -> ", data)

            showPlayers(pixels, playersAddresses, playersColors, data)

            currentCommand = WAIT

        if currentCommand == PRINT_USER:
            print(data)
            currentCommand = WAIT

        if currentCommand == SET_NEW_POINT:
            print("SET_NEW_POINT -> ", data)

            # remove in function
            if (data.lastPosition < 0 and data.currentPosition >= 0):
                pixels[data.stripList[0]] = data.color
                pixels.show()
                time.sleep(1)

            resultOfMoving = 0
            if (doubleColorPoints.get(data.lastPosition) is None):
                resultOfMoving = playerMoveFromOnePlayerPoint(pixels, data.stripList, data.lastPosition,
                                                              data.currentPosition, 1)
            else:
                resultOfMoving = playerMoveFromTwoPlayerPoint(pixels, data.stripLight, data.lastPosition,
                                                              data.currentPosition, 1, data.color,
                                                              doubleColorPoints.pop(data.lastPosition))
            if resultOfMoving != 0:
                doubleColorPoints[data.currentPosition] = resultOfMoving

            currentCommand = WAIT

        if currentCommand == PARTY:
            print("PARTY -> ", data)

            fillAllEffectFromCenter(pixels, playersAddresses, data.color)

            currentCommand = PARTY_2

        if currentCommand == PARTY_2:
            print("PARTY_2 -> ", data)
            turnOffBoard(pixels)
            randomColorAndWhite(pixels, data.color)

        if currentCommand == CLEAR:
            print("CLEAR")

            turnOffBoard(pixels)

            currentCommand = WAIT

        if currentCommand == WAIT:
            print("WAIT")

        if currentCommand == EXIT:
            print("EXIT")

            turnOffBoard(pixels)

            break

        time.sleep(0.7)
