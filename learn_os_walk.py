import os

a_file_path = './learn_decorator.py'
a_directory_path = '.'


def take_a_walk(fp, flag=True):
    for pathname, subdirnames, subfilenames in os.walk(fp, topdown=flag):
        print(pathname)
        print(subdirnames)
        print(subfilenames)
        print('--------------------------------')
    print('What a walk!')


# *Try to walk in a file path
take_a_walk(a_file_path)
# Output Just 'What a walk!'
# Because there are neither subdirnames nor subfilenames in a single file !

# *Try to walk in a directory path
take_a_walk(a_directory_path)
# Output more than Just 'What a walk!'
# Also all the subdirnames and subfilenames in each file tree level.
# BTW if you want to look through all files in a directory, you can add
# another for subfilename in subfilenames loop inside.
