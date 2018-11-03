from colour import Color
import random

def red():
    #hue: 0-10, 346-360
    hue = random.randint(346, 361)
    hue2 = random.randint(0, 11)
    huePicker = random.randint(0,2)
    if huePicker == 0:
        red = Color(hsl=(hue, 1, 0.5))
    else:
        red = Color(hsl=(hue2, 1, 0.5))
    return red

def orange():
    #hue: 11-50
    hue = random.randint(11, 51)
    return Color(hsl=(hue, 1, 0.5))

def yellow():
    #hue: 51-80
    hue = random.randint(51, 81)
    return Color(hsl=(hue, 1, 0.5))

def green():
    #hue: 81-169
    hue = random.randint(81, 170)
    return Color(hsl=(hue, 1, 0.5))

def blue():
    #hue: 170-240
    hue = random.randint(170, 241)
    return Color(hsl=(hue, 1, 0.5))

def violet():
    #hue: 241-345
    hue = random.randint(241, 345)
    return Color(hsl=(hue, 1, 0.5))
