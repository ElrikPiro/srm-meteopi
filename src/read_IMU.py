from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

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
            red,red,red,green,red,red,red,red,
            red,red,red,red,red,red,red,red,
            yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
            yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
            yellow,yellow,yellow,yellow,yellow,yellow,yellow,blue,
            yellow,yellow,yellow,yellow,yellow,yellow,yellow,yellow,
            red,red,red,red,red,red,red,red,
            red,red,red,red,red,red,red,red
            ]
    sense.set_pixels(pixels)
    return;

o = sense.get_orientation()
pitch = o["pitch"]
roll = o["roll"]
yaw = o["yaw"]
print("cabeceo {0} alabeo {1} guiñada {2}".format(pitch,roll,yaw))

sense.clear()
