# -*- coding: utf-8 -*-
__author__ = 'jockay'

import os
import sys


def set_resolution(res=""):
    """
    Sets the resolution of the monitor and writes terminal message to file.

    :param ref : String The refresh rate to set
    """
    if(not(res=="")):
        os.system("xrandr -s {} 2> ../var/monitor_message".format(res))


def set_refresh_rate(ref=""):
    """
    Sets the refresh rate of the monitor and writes terminal message to file.

    Parameters
    ----------
    ref : String
        The refresh rate to set
    """
    if(not(ref=="")):
        os.system("xrandr -r {} 2> ../var/monitor_message".format(ref))

def get_message():
    #print sys.argv[0]
    return


if __name__ == '__main__':
    if(len(sys.argv) >= 2):
        res = sys.argv[1]
    if(len(sys.argv) >= 3):
        ref = sys.argv[2]
    set_resolution(res)
    set_refresh_rate(ref)
    get_message()

