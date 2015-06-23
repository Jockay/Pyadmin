__author__ = 'jockay'

import os


# install package dependencies
dependency_list = ['python-pip',
      'python-pyside']
for item in dependency_list:
    os.system("sudo apt-get install {}".format(item))

# install python library depencencies with pip
pip_list = ['arrow']
for item in dependency_list:
    os.system("sudo pip install {}".format(item))

# create message file for modules
msg_file_list = [ 'find_message',
        'monitor_message',
    ]
for item in dependency_list:
    os.system("sudo pip install {}".format(item))

os.system("sudo chmod 777 var/*")