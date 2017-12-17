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
for i in range(8): #set random green matrix dots
    for j in range(8):
        if randint(0,100) < 30:
            sense.set_pixel(i,j,(0,255,0))

flag = 1
count = 0

while flag:
    for i in range(8): #dim all
        for j in range(8):
            x = sense.get_pixel(i,j)[1]
            if x > 63:
                sense.set_pixel(i,j,(1,x-64,1))
            elif x > 31:
                sense.set_pixel(i,j,(0,x-32,0))
                
    
    for i in range(8): #move green matrix dots
        for j in range(8):
            x = sense.get_pixel(i,j)[1]
            if j>0 and x<63:
                y = sense.get_pixel(i,j-1)
                if y[1]>63 and y[0] < 63:
                    sense.set_pixel(i,j,(255,255,255))

    if count > 100:
        flag = 0
    else:
        if randint(0,100) < 75:
            sense.set_pixel(randint(0,7),0,(255,255,255))
        sleep(.1)
        count = count+1

sense.clear()
