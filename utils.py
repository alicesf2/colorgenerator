from colour import Color
import random

minTempo = 76
midValence = 0.4

def getColors(valence, tempo, energy, mode):
    if mode == 0:
        #get colorscheme COOL AS CENTRAL
        startColor = randomStartCool()
    else:
        #get colorscheme WARM AS CENTRAL
        startColor = randomStartWarm()
    if tempo < minTempo:
        #monochromatic
        return monochromatic(startColor)
    if valence == 0:
        #return acrhomatic color scheme
        return achromatic(startColor)
    elif valence < midValence:
        #return analogous
        return analogous(startColor)
    else:
        #return complimentary
        return complimentary(startColor)
    return []

def analogous(startColor):
    startHue = startColor.hue
    rightHue = startHue + 30
    if rightHue > 360:
        rightHue = rightHue % 360
    leftHue = startHue - 30
    if leftHue < 0:
        leftHue = leftHue + 360
    return [Color(hsl=(leftHue, 1.0, 0.5)).hex_l, startColor.hex_l, Color(hsl=(rightHue, 1.0, 0.5)).hex_l]

def monochromatic(startColor):
    startHue = startColor.hue
    return [startColor.hex_l, Color(hsl=(startHue, 1.0, 0.75)).hex_l, Color(hsl=(startHue, 1.0, 0.90)).hex_l]

def achromatic(startColor):
    startHue = startColor.hue
    return [Color(hsl=(startHue, .6, 1)).hex_l, Color(hsl=(startHue, 0, 0.5)).hex_l, Color(hsl=(startHue, .3, 0)).hex_l]

def complimentary(startColor):
    return []

def whichColor(startColorHue):
    if startColorHue >= 0 and startColorHue <= 10:
        return "red"
    elif startColorHue >= 346 and startColorHue <= 360:
        return "red"
    elif startColorHue >= 11 and startColorHue <= 50:
        return "orange"
    elif startColorHue >= 51 and startColorHue <= 80:
        return "yellow"
    elif startColorHue >= 81 and startColorHue <= 169:
        return "green"
    elif startColorHue >= 170 and startColorHue <= 241:
        return "blue"
    return "violet"

#-----------------------------COLOR CHOOSING------------------------------

def randomStartWarm():
    whichColor = random.randint(0,3)
    if whichColor == 1:
        color = red()
    elif whichColor == 2:
        color = orange()
    else:
        color = yellow()
    return color

def randomStartCool():
    whichColor = random.randint(0,3)
    if whichColor == 1:
        color = green()
    elif whichColor == 2:
        color = blue()
    else:
        color = violet()
    return color

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
