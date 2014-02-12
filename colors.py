# -*- coding: utf-8 -*-

# takes saturation and variance as args and returns an rgb color value for css
def randomcolors(s, v):
    import random
    import colorsys
	#generate a number for the degrees of hue.
    num = random.randint(0, 359)
	# divide it by 360 to get the decimal value
    num /= 360.0
    gratio = 0.618033988749895
	#add the golden ratio and takes the modulus of the total/1 to make the colors generated more pleasing to the eye.
    num += gratio
    num %= 1
	#convert the HSV values to rgb decimals, then format and return a CSS-friendly RGB tag.
    rgb = colorsys.hsv_to_rgb(num, s, v)
    r = str(int(255 * rgb[0]))
    g = str(int(255 * rgb[1]))
    b = str(int(255 * rgb[2]))
    colorcode = "rgb(" + r + ", " + g + ", " + b + ")"
    return colorcode