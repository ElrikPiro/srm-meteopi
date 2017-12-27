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

p = round(sense.get_pressure(),2)
t = round(sense.get_temperature(),2)
h = round(sense.get_humidity(),2)
msg = "Status: "+str(p)+" millibars, "+str(t)+" degrees (Celsius) and "+str(h)+"% relative humidity."
print(msg)
print("Pressure higher than 1000 indicates high probability of clear skies.")
print("temperature is susceptible of showing higher than actual values")
sense.show_message(msg)

sense.clear()
