__author__ = 'jockay'

import os

def install_from_file(file_url=""):
    """
    Installs packages from a file.

    :param file_url: file to install packages from
    """
    if(not(file_url == "")):
        with open(file_url, 'r') as f:
            for line in f:
                if not (line[0] == '#') and not (line == ''):
                    os.system('sudo aptitude install -y {0}'.format(line))
