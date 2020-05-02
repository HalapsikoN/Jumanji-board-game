# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import threading

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21

# The number of NeoPixels
num_pixels = 14

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.05, auto_write=False, pixel_order=ORDER
)


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


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

#turn off board
def turnOffBoard(pixels):
    pixels.fill((0,0,0))
    pixels.show()
    
#rainbow standart tainbow rownd
def standartFunction(pixels):
    rainbow_cycle(0.006)
    pixels.show()

def playersOnOnePoint(pixels, billAddreses, position, savedColor, colorOnPoint, event):
    wait=0.5
    while not event.is_set():
        pixels[billAddreses[position]]=savedColor
        pixels.show()
        time.sleep(wait)
        pixels[billAddreses[position]]=colorOnPoint
        pixels.show()
        time.sleep(wait)
    
def isPlayerOnPoint(pixels, position):
    return pixles[position]==(0,0,0)

def playerMove(pixels, addressList, startPosition, endPosition, step):
    color=pixels[addressList[startPosition]]    
    wait=0.5
    
    currentPosition=startPosition
    nextPosition=startPosition+step
    
    savedColor=0
    
    while currentPosition!=endPosition:
        if savedColor!=0:
            pixels[addressList[currentPosition]]=savedColor
            savedColor=0
        else:
            pixels[addressList[currentPosition]]=(0,0,0) 
        
        if nextPosition>=len(addressList) or nextPosition<0:
            pixels.show()
            time.sleep(wait)
            break
        
        if pixels[addressList[nextPosition]]!=(0,0,0):
            savedColor=pixels[addressList[nextPosition]]      
        
        pixels[addressList[nextPosition]]=color
        
        currentPosition+=step
        nextPosition+=step
        pixels.show()
        time.sleep(wait)
    
    return savedColor


def playerMove2(pixels, billAddreses, startAddress, endAddress, step, event):
    savedColor=playerMove(pixels, billAddreses, startAddress, endAddress, step)
    currentColor=pixels[billAddreses[endAddress]]
    if savedColor!=0:
        event=event
        thread=threading.Thread(target=playersOnOnePoint, args=(pixels, billAddreses, endAddress, savedColor, currentColor, event))
        thread.start()
    return {billAddreses[endAddress] : [savedColor, currentColor]}

#while True:
    # Comment this line out if you have RGBW/GRBW NeoPixels
    #pixels.fill((255, 0, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((255, 0, 0, 0))
    #pixels.show()
    #time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    #pixels.fill((0, 255, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 255, 0, 0))
    #pixels.show()
    #time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    #pixels.fill((0, 0, 255))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 0, 255, 0))
    #pixels.show()
    #time.sleep(1)
    

    #rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
print("start")

#pixels.fill((0,0,0))
#pixels.show()
# 
# for i in range(85):
#     pixels[5]=wheel(i)
#     pixels.show()
#     time.sleep(0.01)
#     standartFunction(pixels)

# turnOffBoard(pixels)

# for i in range(10):
#     playersOnOnePoint(pixels, 5, (255,30,0), (255,0,0))

billAddreses=[1, 2, 3, 4, 5 ,6 ,7 ,8]

pixels[2]=(255, 30, 0)
pixels[8]=(255, 0, 0)
pixels.show()
time.sleep(3)

startAddress=1
endAddress=7
event=threading.Event()

# savedColor=playerMove(pixels, billAddreses, startAddress, endAddress, 1)
# if savedColor!=0:
#     event=event
#     thread=threading.Thread(target=playersOnOnePoint, args=(pixels, billAddreses, endAddress, savedColor, pixels[billAddreses[endAddress]], event))
#     thread.start()

mapElement=playerMove2(pixels, billAddreses, startAddress, endAddress, 1, event)

print(mapElement.get(8) is None)
print(mapElement.get(2) is None)

time.sleep(6)
event.set()

# pixels.show()
#for i in range(50):
#    rainbow_cycle(0)
#time.sleep(1)

#pixels[5]=(0, 0, 0)
#pixels.show()

print("end")
    
    
    
    
    
    