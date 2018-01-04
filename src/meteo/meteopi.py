#!/usr/bin/python3
from sense_hat import SenseHat,  ACTION_RELEASED
from time import sleep
from random import randint
import datetime

sense = SenseHat()

r = (153,0,0)
b = (0,0,153)
g = (0,153,0)
w = (153,153,153)
y = (153,153,0)
o = (153,76,0)
v = (76,0,153)
n = (0,0,0)
t = (0,153,153)

altitude = 0#TBA-ALTITUDE#
data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
FSM = 0
mutex = 0
measurements = 0

def left(event):
    global FSM, mutex
    if mutex == 1 or event.action!=ACTION_RELEASED:
        return;
    elif FSM == 2:
        FSM = 3
        right(event)
    elif FSM == 3:
        FSM = 1
        OK(event)
    elif FSM == 4:
        FSM = 2
        right(event)
    return;

def right(event):
    global FSM, mutex
    if mutex == 1 or event.action!=ACTION_RELEASED:
        return;
    elif FSM == 2:
        mutex = 1
        sleep(0.5)
        FSM = 3
        print("Menu: Pressure")
        sense.clear()
        pixels = [
                n,n,n,n,n,n,n,n,
                n,n,n,n,n,n,n,w,
                n,n,w,w,w,w,n,n,
                n,w,n,r,n,n,w,n,
                w,n,v,b,v,n,n,w,
                n,n,n,b,n,n,n,n,
                n,n,n,b,n,n,n,n,
                n,n,n,b,n,n,n,n
                ]
        sense.set_pixels(pixels)
        mutex = 0
    elif FSM == 3:
        mutex = 1
        sleep(0.5)
        FSM = 4
        print("Menu: Humidity")
        sense.clear()
        pixels = [
                n,n,n,n,n,n,n,n,
                n,n,n,t,t,n,n,n,
                n,n,n,t,t,n,n,n,
                n,n,t,t,t,t,n,n,
                n,n,t,t,t,t,n,n,
                n,t,t,t,t,t,t,n,
                n,t,t,t,t,t,t,n,
                n,n,t,t,t,t,n,n
                ]
        sense.set_pixels(pixels)
        mutex = 0
    elif FSM  == 4:
        FSM = 1
        OK(event)
    return;

def OK(event):
    global FSM, mutex
    if mutex == 1 or event.action != ACTION_RELEASED:
        return;
    elif FSM == 1:
        mutex = 1
        sleep(0.5)
        FSM = 2
        print("Menu: Temperature")
        sense.clear()
        pixels = [
                n,n,n,b,b,n,n,n,
                n,n,n,b,b,n,n,w,
                n,n,n,b,b,w,w,n,
                n,n,n,b,b,w,n,n,
                n,n,n,b,b,w,w,n,
                n,n,b,r,r,b,n,n,
                n,n,b,r,r,b,n,n,
                n,n,n,b,b,n,n,n
                ]
        sense.set_pixels(pixels)
        mutex = 0
    elif FSM == 2:
        mutex = 1
        sleep(0.5)
        sense.clear()
        print("temperature: "+str(round(sense.get_temperature(),2))+" C")
        sense.show_message(str(round(sense.get_temperature(),2))+" Celsius")
        mutex = 0
        FSM = 1
        show_forecast(data,measurements)
    elif FSM == 3:
        mutex = 1
        sleep(0.5)
        sense.clear()
        print("Pressure: "+str(round(sense.get_pressure(),2))+" Millibars")
        sense.show_message(str(round(sense.get_pressure(),2))+" Millibars")
        sense.show_message(str(round(sense.get_pressure()*0.0295301,2))+" Inches")
        ls = least_squares(data,measurements)
        sense.show_message("Trend: "+str(round(ls[1],3))+" Inches per hour.")
        mutex = 0
        FSM = 1
        show_forecast(data,measurements)
    elif FSM == 4:
        mutex = 1
        sleep(0.5)
        sense.clear()
        print("Humidity: "+str(round(sense.get_humidity(),2))+" %")
        sense.show_message(str(round(sense.get_humidity(),2))+" %")
        mutex = 0
        FSM = 1
        show_forecast(data,measurements)
    return;

def random_color():
    random_red = randint(0,255)
    random_green = randint(0,255)
    random_blue = randint(0,255)
    return (random_red,random_green,random_blue)

def show_sun():
    print("Sunny")
    pixels = [
            y,b,b,b,b,b,b,y,
            b,y,b,b,b,b,y,b,
            b,b,b,y,y,b,b,b,
            b,b,y,o,o,y,b,b,
            b,b,y,o,o,y,b,b,
            b,b,b,y,y,b,b,b,
            b,y,b,b,b,b,y,b,
            y,b,b,b,b,b,b,y
            ]
    sense.set_pixels(pixels) 
    return;

def show_clouds():
    print("Cloudy")
    pixels = [
            b,b,b,b,b,b,b,b,
            b,b,w,b,w,b,b,b,
            b,w,w,w,w,w,b,b,
            w,w,w,w,w,w,w,b,
            b,w,w,w,w,w,b,b,
            b,b,w,b,w,b,b,b,
            b,b,b,b,b,b,b,b,
            b,b,b,b,b,b,b,b
            ]
    sense.set_pixels(pixels)
    return;

def show_clouds_sun():
    print("Ambiguous")
    pixels = [
            b,b,b,b,b,b,b,b,
            b,b,w,b,w,y,y,b,
            b,w,w,w,w,w,o,y,
            w,w,w,w,w,w,w,y,
            b,w,w,w,w,w,y,b,
            b,b,w,b,w,b,b,b,
            b,b,b,b,b,b,b,b,
            b,b,b,b,b,b,b,b
            ]
    sense.set_pixels(pixels)
    return;

def show_storm():
    print("Stormy")
    pixels = [
            n,n,n,n,n,n,n,n,
            n,n,w,n,w,n,n,n,
            n,w,w,w,w,w,n,n,
            w,w,w,w,w,w,w,n,
            n,w,y,y,w,w,n,n,
            n,n,w,y,y,t,n,n,
            t,n,n,y,n,n,t,n,
            n,t,n,y,t,n,n,n
            ]
    sense.set_pixels(pixels)
    return;

def show_rain():
    print("Rainy")
    pixels = [
            n,n,n,n,n,n,n,n,
            n,n,w,n,w,n,n,n,
            n,w,w,w,w,w,n,n,
            w,w,w,w,w,w,w,n,
            n,w,w,w,w,w,n,n,
            n,t,w,t,w,t,n,n,
            t,n,t,n,t,n,n,n,
            n,t,n,t,n,n,n,n
            ]
    sense.set_pixels(pixels)
    return;

def least_squares(d,m):
    #Least squares adjustment
    x = 0;
    y = 0;
    xy = 0;
    x2 = 0;
    c = 0;
    k = 30;
    last_value = d[m-1]
    if m < 24 and m>1:
        for i in range(0,m):
            x = x+(i)
            y = y+(d[i])
            xy = xy+(i*d[i])
            x2 = x2+(i*i)
        c = (xy-((x*y)/m))/(x2-((x*x)/m))
        k = (y/m)-c*(x/m)
    elif m >= 24:
        for i in range(0,24):
            x = x+(i)
            y = y+(d[i])
            xy = xy+(i*d[i])
            x2 = x2+(i*i)
        c = (xy-((x*y)/24))/(x2-((x*x)/24))
        k = (y/24)-c*(x/24)
    
    print("Pressure for the next hour predicted to be: "+str(c*(m+1)+k))
    print("Pressure in 12 hours predicted to be:"+str(c*(m+12)+k))
    print("Pressure in 24 hours predicted to be:"+str(c*(m+24)+k))
    print("trend: "+str(c)+" constant: "+str(k))
    print("DEBUG: "+str(x)+" "+str(y)+" "+str(xy)+" "+str(x2))
    print("Please note that this is a linear estimation.")
    
    return [last_value,c]

def show_forecast(d,m):
    le = least_squares(d,m)
    
    if le[0] > 30.00 and le[0] < 30.20 and le[1] < 0.01 and le[1] > -0.01:
        show_sun()
    elif le[0] > 30.00 and le[0] < 30.20 and le[1] > 0.03:
        show_sun()
    elif le[0] > 30.00 and le[0] < 30.20 and le[1] < -0.03:
        show_clouds()
    elif le[0] > 30.20 and le[1] < -0.03:
        show_clouds()
    elif le[0] > 30.20 and le[1] > -0.01:
        show_sun()
    elif le[0] < 29.80 and le[1] < -0.03:
        show_storm()
    elif le[0] < 29.80 and le[1] > 0.03:
        show_clouds()
    elif le[0] < 30.00 and le[1] > 0.01:
        show_sun()
    elif le[0] < 30.00 and le[1] < -0.03:
        show_rain()
    elif le[0] < 30.00 and le[1] < -0.01:
        show_rain()
    else:
        show_clouds_sun()
    return;

sense.stick.direction_left = left
sense.stick.direction_right = right
sense.stick.direction_middle = OK
sense.stick.direction_up = sense.clear

#init
measurements = 0
counter = 0
#sense.show_message("Welcome to meteopi, use the joystick to navigate. Forecasting will take several hours to start showing reliable data.",scroll_speed=0.05)
sense.clear()
sense.get_pressure()


#while || FSM1 Standby
FSM = 1
while True:
    now = datetime.datetime.now()
    strnow = now.strftime("%d-%m-%Y %H:%M")
    
    if FSM == 1:
        mutex = 1
        print(strnow)
        sense.show_message(strnow,scroll_speed=0.05)
        show_forecast(data,measurements)
        mutex = 0
    
    if counter%60 == 0:
        if measurements < 24:
            data[measurements] = sense.get_pressure()*0.0295301
            print(str(data[measurements])+" inches, incomplete set")
            measurements = measurements+1
        else:
            for i in range(23):
                data[i] = data[i+1]
            data[23] = sense.get_pressure()*0.0295301
            print(str(data[23])+" inches")
        if FSM == 1:
            mutex = 1
            show_forecast(data,measurements)
            mutex = 0
    
    counter=(counter+1)%60
    print(str(60-counter)+" minutes to next measure.")
    sleep(60)
