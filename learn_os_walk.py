__author__ = 'Anqi Wu'

import os

a_directory_path = './learn_os_walk'
a_file_path = './learn_os_walk.py'  # same as a_file_path = __file__


def take_a_walk(fp, topdown_flag=False):
    print(f'\ntopdown_flag:{topdown_flag}\n')
    for pathname, subdirnames, subfilenames in os.walk(fp, topdown=topdown_flag):
        print(pathname)
        print(subdirnames)
        print(subfilenames)
        print('--------------------------------')
    print('What a walk!')


# *Try to walk in a file path
take_a_walk(a_file_path)
# Output Just 'What a walk!'
# Because there are neither subdirnames nor subfilenames in a single file !
# It is like:
# for i in []:
#     print('hi!')  # We are not going to execute this line.


# *Try to walk in a directory path
take_a_walk(a_directory_path)
# Output more than Just 'What a walk!'
# Also all the subdirnames and subfilenames in each file tree level.
# BTW if you want to look through all files in a directory, you can add
# another for subfilename in subfilenames loop inside.

# *Try to list all files and directories in a directory path
print('\n')
print(os.listdir(a_directory_path))
print('\n')
