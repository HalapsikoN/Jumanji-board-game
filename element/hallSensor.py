import RPi.GPIO as GPIO
import random

def checkPin(number):
    GPIO.setup(number, GPIO.IN)
    trueCounter = 0
    falseCounter = 0
    for i in range(19):
        if (GPIO.input(number) == True):
            trueCounter += 1
        else:
            falseCounter += 1
    if trueCounter >= falseCounter:
        return 1
    else:
        return 0


def getPlayers():
    GPIO.setmode(GPIO.BCM)
    result = []

    player0pin = 16
    player1pin = 20
    player2pin = 19
    player3pin = 26

    result.append(checkPin(player0pin))
    result.append(checkPin(player1pin))
    result.append(checkPin(player2pin))
    result.append(checkPin(player3pin))
    GPIO.cleanup()

    while result.count(1) < 2:
        result[random.randrange(len(result))] = 1

    return result
