def counter(func):

    count = 0

    def inner():
        nonlocal count
        count +=1
        func()
        print(f'Function called {count} times!')

    return inner

@counter
def say_hi():
    print('Hello!')

@counter
def say_bye():
    print('Bye!')

say_bye()
say_bye()
say_bye()

print(100*"*")

say_hi()
say_hi()
say_hi()
say_hi()
say_hi()