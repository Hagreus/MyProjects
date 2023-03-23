try:
    f = open('file.txt', 'r')

    for line in f.readlines():
        print(line, end='')

except FileNotFoundError:
    print('Error, file not found!')
