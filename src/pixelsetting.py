from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)
yellow = (255,255,0)
orange = (255,127,0)
violet = (139,0,255)

def random_color():
    random_red = randint(0,255)
    random_green = randint(0,255)
    random_blue = randint(0,255)
    return (random_red,random_green,random_blue)

def spain_flag():
    pixels = [
            red,red,red,red,red,red,red,red,
            red,red,red,red,red,red,red,red,
            yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
            yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
            yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
            yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
            red,red,red,red,red,red,red,red,
            red,red,red,red,red,red,red,red
            ]
    sense.set_pixels(pixels)
    return;

spain_flag()
sleep(3)
sense.clear()
