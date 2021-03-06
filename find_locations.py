#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# Import
import logging
from executor.ActionScheduler import ActionReservoirFullError, ActionAlreadyExists
from media.MediaFinder import MediaFinder
import langdetect.lang_detect_exception
import learning
import tools.strings as pystr
import random
from langdetect import detect
from pyInstaBot.db.obj.Comment import Comment


####################################################
# Globals
####################################################


####################################################
# Functions
####################################################


####################################################
# Main function
####################################################


# Find new medias from various sources
def find_locations(instagram_connector, config, query):
    """
    Find new medias from various sources
    :param config:
    :return:
    """
    # For each result
    for item in instagram_connector.search_location(query)['items']:
        print(u"Title: \"{}\", Subtitle: \"{}\"".format(item['title'], item['subtitle']))
    # end for
# end find_locations
