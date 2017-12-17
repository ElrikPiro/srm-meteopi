from sense_hat import SenseHat
import time
sense = SenseHat()


sense.clear((255,0,0))
time.sleep(.5)

sense.clear((255,127,0))
time.sleep(.5)

sense.clear((255,255,0))
time.sleep(.5)

sense.clear((0,255,0))
time.sleep(.5)

sense.clear((0,0,255))
time.sleep(.5)

sense.clear((139,0,255))
time.sleep(.5)

sense.clear((0,0,0))
