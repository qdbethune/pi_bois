from gpiozero import LED
from time import sleep

red = LED(12)
green = LED(13)
blue = LED(18)
yel = LED(19)

while True:
    for i in range(2):
        red.off()
        green.off()
        blue.off()
        yel.off()
        sleep(.2)
        # White
        red.on()
        green.on()
        blue.on()
        yel.on()
        sleep(.2)
    red.off()
    sleep(.1)
    green.off()
    sleep(.1)
    yel.off()
    sleep(.1)
    blue.off()
    red.on()
    sleep(.1)
    green.on()
    sleep(.1)
    yel.on()
    sleep(.1)
    blue.on()
    sleep(.2)
    blue.off()
    sleep(.1)
    yel.off()
    sleep(.1)
    green.off()
    sleep(.1)
    red.off()
    sleep(1)
    