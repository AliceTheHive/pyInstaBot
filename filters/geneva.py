#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# Imports
import math
import numpy as np
import sys, os


# Check color
def checkColor(color):
    """
    Check color
    :param color:
    :return:
    """
    if color > 255:
        return 255
    # end if
    if color < 0:
        return 0
    # end if
    return color
# checkColor


# Geneva filter
def geneva(img, params):
    """
    Geneva filter
    :param img:
    :param brownfusion:
    :param blackoutside:
    :return:
    """
    # Info
    image_width = img.shape[1]
    image_height = img.shape[0]

    # Initialize value
    alpha = 1.775
    beta = -40

    # Brown fusion
    if 'brownfusion' in params:
        brownfusion = params['brownfusion']
    else:
        brownfusion = 25
    # end if

    # Black outside
    if 'blackoutside' in params:
        blackoutside = params['blackoutside']
    else:
        blackoutside = 100
    # end if

    # Distance max
    dmax = math.sqrt(math.pow(image_width, 2) + math.pow(image_height, 2))

    # Iterate over all the pixels and convert them to gray.
    for x in range(image_width):
        for y in range(image_height):
            # Distance
            dx = math.fabs(x - (image_width / 2.0))
            dy = math.fabs(y - (image_height / 2.0))
            distance = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))

            # Get the pixel and verify that is an RGB value
            pixel = img[x, y]

            # Colors
            r = alpha * pixel[0] + beta
            g = alpha * pixel[1] + beta
            b = alpha * pixel[2] + beta

            # Color average
            average = (r + g + b) / 3.0

            # Brown fusion
            r = average
            g = average
            b = average + brownfusion

            # Black outside
            r -= ((blackoutside / dmax) * distance)
            g -= ((blackoutside / dmax) * distance)
            b -= ((blackoutside / dmax) * distance)

            # Check bounds
            r = checkColor(r)
            g = checkColor(g)
            b = checkColor(b)

            if len(pixel) >= 3:
                print(pixel)
                # Create a new tuple representing the new color.
                newColor = np.array([int(r), int(g), int(b)])
                img[x, y, 0] = newColor[0]
                img[x, y, 1] = newColor[1]
                img[x, y, 2] = newColor[2]
            # end if
        # end for
    # end for
    return img
# end geneva
