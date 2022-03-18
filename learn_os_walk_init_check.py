import os

a_directory_path = './learn_os_walk'

for pathname, subdirnames, subfilenames in os.walk(a_directory_path):
    for subdirname in subdirnames:
        init_filepath = os.path.join(pathname, subdirname, '__init__.py')
        if not os.path.exists(init_filepath):
            print(f'Create a new empty [{init_filepath}] file.')
            with open(init_filepath, 'w') as f:
                pass
