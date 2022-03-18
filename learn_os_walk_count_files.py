import os

a_directory_path = './learn_os_walk'
total_file = 0

for pathname, subdirnames, subfilenames in os.walk(a_directory_path):
    for subfilename in subfilenames:
        if subfilename.endswith('.txt'):
            total_file += 1
print(f'\n{total_file}\n')
