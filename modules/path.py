__author__ = 'jockay'

import os


def add_to_path(url=""):
    """
    Adds an url to system PATH variable.

    :param url: url to add to PATH
    """
    if(not(url=="")):
        os.system('export PATH=$PATH:{} 2> path_message'.format(url))