grey_prefix = '\033[90m'
red_prefix = '\033[91m'
green_prefix = '\033[92m'
yellow_prefix = '\033[93m'
indigo_prefix = '\033[94m'
purple_prefix = '\033[95m'
blue_prefix = '\033[96m'


test_string = 'Colorful strings~~~'
for i in range(7):
    color_prefix = '\033[9' + str(i) + 'm'
    print(color_prefix + test_string)
