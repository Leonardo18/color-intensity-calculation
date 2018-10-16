import sys
import re
import math


def format_hex_color(hex_color):
    return hex_color.replace("#", "")


def fetchRedFromHexColor(hex_color):
    if len(hex_color) == 6:
        # #RRGGBB
        red = int(hex_color[:2], 16)
    elif len(hex_color) == 3:
        red = int(hex_color[0] + hex_color[0], 16)
    return red


def fetchGreenFromHexColor(hex_color):
    if len(hex_color) == 6:
        # #RRGGBB
        green = int(hex_color[2:4], 16)
    return green


def fetchBlueFromHexColor(hex_color):
    if len(hex_color) == 6:
        # #RRGGBB
        blue = int(hex_color[4:6], 16)
    return blue


def perceivedBrightness(r, g, b):
    return int(math.sqrt(
        r * r * .299 +
        g * g * .587 +
        b * b * .114
    ))


hex_color = sys.argv[1]


red = 0
green = 0
blue = 0


match = re.search(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', hex_color)


if match:            
    hex_color = format_hex_color(hex_color)
    
    
    red = fetchRedFromHexColor(hex_color)
    print 'red: ' + str(red)
    green = fetchGreenFromHexColor(hex_color)
    print 'green: ' + str(green)
    blue = fetchBlueFromHexColor(hex_color)
    print 'blue: ' + str(blue)
    

    color_intensity = perceivedBrightness(red, green, blue)

    
    print color_intensity > 130 and "The color intensity is closer to white" or "The color intensity is closer to black"
else:
    print 'Hex color is not valid'