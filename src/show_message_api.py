from sense_hat import SenseHat
sense = SenseHat()

red = (255,0,0)
yellow = (255,255,0)

while True:
    sense.show_message("Hello world", text_colour=yellow, back_colour=red, scroll_speed=0.05)
