#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : pyTweetBot.py
# Description : pyTweetBot main execution file.
# Auteur : Nils Schaetti <n.schaetti@gmail.com>
# Date : 01.05.2017 17:59:05
# Lieu : Nyon, Suisse
#
# This file is part of the pyTweetBot.
# The pyTweetBot is a set of free software:
# you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyTweetBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with pyTweetBar.  If not, see <http://www.gnu.org/licenses/>.
#

# Import
import os
import logging
import tools.strings as pystr
import skimage
import skimage.io
from filters import *


#


# Apply filter
def apply_filter(image_path, filter):
    """
    Apply filter
    :param input:
    :param filter:
    :return:
    """
    # Output path
    file_ext =  os.path.splitext("path_to_file")[1]
    output_path = os.path.splitext("path_to_file")[0] + "_" + filter + file_ext

    # Load image
    img = skimage.io.imread(image_path)

    # Filter function
    img = geneva(img, {})
    print(output_path)
    # Save image
    skimage.io.imsave(output_path, img)
    exit()
    return output_path
# end apply_filter

