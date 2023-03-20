try:
    with open('file.txt', 'r') as file:
        for line in file.readlines():
            print(line, end='')

except FileNotFoundError:
    print('Error, file not found!')