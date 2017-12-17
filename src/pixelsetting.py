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
for i in range(0,7): #set random green matrix dots
    for j in range(0,7):
        if randint(0,100) < 30:
            sense.set_pixel(i,j,(0,255,0))

flag = 1
count = 0

while flag:
    for i in range(0,7): #dim all
        for j in range(0,7):
            x = sense.get_pixel(i,j)[1]
            if x > 31:
                sense.set_pixel(i,j,(0,x-32,0))
            else:
                count = count+1
    
    for i in range(0,7): #move green matrix dots
        for j in range(0,7):
            x = sense.get_pixel(i,j)[1]
            if i>0 and :
                y = sense.get_pixel(i-1,j)
                if y[1]>31 and y[0] < 31:
                    sense.set_pixel(i,j,(255,y+32,255))

    if count > 61:
        flag = 0
    else:
        count = 0
        sleep(.5)

sense.clear()
