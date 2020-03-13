COLOR_CODES = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']


def value(colors):
    return int(str(COLOR_CODES.index((colors[0:1])[0])) + str(COLOR_CODES.index((colors[1:2])[0])))