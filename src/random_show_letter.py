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


sense.show_letter("R", random_color())
sleep(1)

sense.show_letter("o", random_color())
sleep(1)

sense.show_letter("s", random_color())
sleep(1)

sense.show_letter("i", random_color())
sleep(1)

sense.show_letter("t", random_color())
sleep(1)

sense.show_letter("a", random_color())
sleep(1)

sense.clear()
