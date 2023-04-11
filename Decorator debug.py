def debug(func):
    def inner(*args, **kwargs):
        print(f'Input: {args}')
        func(*args, **kwargs)
        print(f'Return: {func(*args, **kwargs)}')

    return inner


@debug
def odd(x, y):
    """a function that takes 2 arguments (numbers) and adds them"""

    return x + y


odd(3, 5)
