__author__ = 'jockay'

import os
import sys


def search_in_filesystem(s=""):
    if(not(s == "")):
        os.system("find / {0} > ../var/find_message".format(s))


def search_by_url(url="", s=""):
    if(not(s == "") and not(url == "")):
        os.system("find {0} -name {1} > ../var/find_message".format(url, s))


if __name__ == '__main__':
    search_by_url(sys.argv[1], sys.argv[2])