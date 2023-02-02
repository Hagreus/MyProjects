class word():
    def __init__(self, password):
        self.password = password

    def characters(self):
        if len(self.password) < 12:
            return False
        return

    def numbers(self):
        if self.password.isalpha():
            return False
        return

    def letters(self):
        if self.password.isdigit():
            return False
        return

    def lower_case(self):
        if self.password.islower():
            return False
        return

    def space(self):
        if ' ' in self.password:
            return False
        return

while True:
    s = input('Введите пароль: ')
    w1 = word(s)
    if w1.characters() is False:
        print('Пароль должен >12 символов!')

    elif w1.letters() is False:
        print('В пароле должны быть буквы!')

    elif w1.numbers() is False:
        print('В пароле должны быть цифры!')

    elif w1.lower_case() is False:
        print('В пароле должна быть хотя бы одна заглавная буква!')

    elif w1.space() is False:
        print('В пароле не должно быть пробелов!')

    else:
        print('Ваш пароль создан')
        break