import random

def game():
    # Список слов
    LST = ['car', 'phone', 'complement', 'english']
    word = random.choice(LST)
    hidden_word = len(word) * '*'

    # Кол-во попыток
    attempts = int(input('Введите кол-во попыток: '))
    # Основной цикл игры
    while True:
        # Ввод буквы/слова пользователя
        letter = input('Введите букву: ').lower()

        if len(letter) == 1:
            if letter in hidden_word:
                print('Вы уже писали эту букву!')
                continue
            elif letter in word:
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
                print('Такой буквы в слове нет')
                print(f'Попыток осталось: {attempts}\n')

                if attempts == 0:
                    print('Вы проиграли :(')
                    break

        elif len(letter) > 1:
            if letter == word:
                print(f'Вы угадали слово {word}!')
                break

            else:
                attempts -= 1
                print('Вы не угадали слово :(')
                print(f'Попыток осталось: {attempts}\n')

                if attempts == 0:
                    print('Вы проиграли :(')
                    break

            continue

if __name__ == '__main__':
    game()
