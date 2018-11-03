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
    if (energy >= 0.9):
        return complementary(startColor.hue)
    if tempo < minTempo:
        #monochromatic
        return monochromatic(startColor.hue)
    if valence == 0:
        #return acrhomatic color scheme
        return achromatic(startColor.hue)
    elif valence < midValence:
        #return analogous
        return analogous(startColor.hue, valence)
    else:
        #return complimentary
        return complementary(startColor.hue, valence)
    return []

def analogous(startHue, valence):
    startHue = startHue * 360

    rightHue = startHue + 60
    if rightHue > 360:
        rightHue = rightHue % 360

    rightRightHue = startHue + 30
    if rightRightHue > 360:
        rightRightHue = rightRightHue % 360

    leftHue = startHue - 60
    if leftHue < 0:
        leftHue = leftHue + 360

    leftLeftHue = startHue - 30
    if leftLeftHue < 0:
        leftLeftHue = leftLeftHue + 360
    return [Color(hsl=(leftHue/360.0, valence, 0.3)).hex_l,
    Color(hsl=(leftLeftHue/360.0, valence, 0.3)).hex_l,
    Color(hsl=(startHue/360.0, valence, 0.3)).hex_l,
    Color(hsl=(rightRightHue/360.0, valence, 0.3)).hex_l,
    Color(hsl=(rightHue/360.0, valence, 0.3)).hex_l]

def monochromatic(startHue):
    return [Color(hue = startHue, saturation = 1.0, luminance = 0.15).hex_l,
    Color(hue = startHue, saturation = 1.0, luminance = 0.25).hex_l,
    Color(hue = startHue, saturation = 1.0, luminance = 0.5).hex_l,
    Color(hue = startHue, saturation = 1.0, luminance = 0.75).hex_l,
    Color(hue = startHue, saturation = 1.0, luminance = 0.90).hex_l]

def achromatic(startHue):
    return [Color(hsl=(startHue, 0, 0.8)).hex_l,
    Color(hsl=(startHue, 0, 0.5)).hex_l,
    Color(hsl=(startHue, 0, 0.3)).hex_l,
    Color(hsl=(startHue, 0, 0.1)).hex_l,
    Color(hsl=(startHue, 0, 0)).hex_l]

def complementary(startHue, valence):
    print(startHue)
    rightHue = (startHue*360) + 180
    if rightHue > 360:
        rightHue = rightHue % 360
    return [Color(hsl=(startHue, valence, 0.75)).hex_l,
     Color(hsl=(startHue, valence, 0.5)).hex_l,
     Color(hsl=(startHue, valence, 0.25)).hex_l,
     Color(hsl=(rightHue/360.0, valence, 0.5)).hex_l,
     Color(hsl=(rightHue/360.0, valence, 0.75)).hex_l]

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
        red = Color(hsl=(hue/360.0, 1, 0.5))
    else:
        red = Color(hsl=(hue2/360.0, 1, 0.5))
    return red

def orange():
    #hue: 11-50
    hue = random.randint(11, 51)
    return Color(hsl=(hue/360.0, 1, 0.5))

def yellow():
    #hue: 51-80
    hue = random.randint(51, 81)
    return Color(hsl=(hue/360.0, 1, 0.5))

def green():
    #hue: 81-169
    hue = random.randint(81, 170)
    return Color(hsl=(hue/360.0, 1, 0.5))

def blue():
    #hue: 170-240
    hue = random.randint(170, 241)
    return Color(hsl=(hue/360.0, 1, 0.5))

def violet():
    #hue: 241-345
    hue = random.randint(241, 345)
    return Color(hsl=(hue/360.0, 1, 0.5))
