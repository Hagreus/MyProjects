import random
def game():
    # Список слов
    LST = ['car', 'phone', 'complement', 'english']
    word = random.choice(LST)
    hidden_word = len(word)*'*'

    hidden_lst = []
    for i in hidden_word:
        hidden_lst.append(i)

    # Кол-во попыток
    attempts = int(input('Введите кол-во попыток: '))

    # Основной цикл игры
    while True:
        # Ввод буквы/слова пользователя
        letter = input('Введите букву: ')
        # Проверяем, если ввод пользователя слово, и оно верное, тогда пишем 'Да, вы угадали целое слово!' и заканчиваем цикл
        if letter == word:
            print('Да, вы угадали!')
            break
        elif type(letter) == int:
            attempts -=1
            print('Вводите только буквы!')
            print(f'Кол-во оставшихся попыток: {attempts}')
        elif len(letter) == 1:
            if letter in word:
                new = ''

                for i in range(len(word)):
                    if letter == word[i]:
                        new += letter
                    else:
                        new += hidden_word[i]
                hidden_word = new
                print(new)
                if new == word:
                    print('Вы выиграли!')
                    break

            else:
                attempts -= 1
                print('Такой буквы нет')
                print(f'Кол-во оставшихся попыток: {attempts}')
        if attempts == 0:
            print('Вы проиграли:(')
            break

game()