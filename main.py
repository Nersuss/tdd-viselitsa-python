import random, os

clear = lambda: os.system('cls')

def str_is_valid(char):
    char = char.lower()
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    if((len(char) == 1) and (char in alphabet)):
        return True
    return False

def load_words(path):
    with open(path, 'r', encoding="utf-8") as file:
        return [row.strip() for row in file]

words = load_words('words.txt')

def get_random_word(words):
    return words[random.randint(0, len(words) - 1)]

random_word = get_random_word(words)

def char_contains_in_word(chars, word):
    if word.__contains__(chars):
        return True
    return False

def print_man(count_mistakes):
    if count_mistakes == 0:
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('------------')
    elif count_mistakes == 1:
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('------------')
    elif count_mistakes == 2:
        print('|-------')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('------------')
    elif count_mistakes == 3:
        print('|-------')
        print('|      |')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('------------')
    elif count_mistakes == 4:
        print('|-------')
        print('|      |')
        print('|      0')
        print('|')
        print('|')
        print('|')
        print('|')
        print('------------')
    elif count_mistakes == 5:
        print('|-------')
        print('|      |')
        print('|      0')
        print('|      |')
        print('|      |')
        print('|')
        print('|')
        print('------------')
    elif count_mistakes == 6:
        print('|-------')
        print('|      |')
        print('|      0')
        print('|     /|')
        print('|      |')
        print('|')
        print('|')
        print('------------')
    elif count_mistakes == 7:
        print('|-------')
        print('|      |')
        print('|      0')
        print('|     /|\\')
        print('|      |')
        print('|')
        print('|')
        print('------------')
    elif count_mistakes == 8:
        print('|-------')
        print('|      |')
        print('|      0')
        print('|     /|\\')
        print('|      |')
        print('|     /')
        print('|')
        print('-----------')
    elif count_mistakes == 9:
        print('|-------')
        print('|      |')
        print('|      0')
        print('|     /|\\')
        print('|      |')
        print('|     / \\')
        print('|')
        print('-----------')

open_chars = []
count_mistakes = 0

def print_word(open_chars, word):
    print('Слово: ', end='')
    for i in range(0, len(word)):
        if open_chars.__contains__(word[i]) :
            print(word[i], end='')
        else:
            print('_', end='')
    print()

def is_end_game(open_chars, word):
    for i in range(0, len(word)):
        if not open_chars.__contains__(word[i]):
            return False
    return True

if __name__ == '__main__':
    print('Игра в Виселицу началась!')
    while count_mistakes < 9 and is_end_game(open_chars, random_word) == False:
        print_man(count_mistakes)
        print_word(open_chars, random_word)

        char = input('Введите букву:')
        while ((str_is_valid(char) == False) or (open_chars.__contains__(char))):
            print('Введен некорректный символ')
            char = input('Введите букву:')
        clear()
        if char_contains_in_word(char, random_word):
            open_chars.append(char)
            print('Вы угадали букву!')
        else:
            count_mistakes+=1
            print('Вы не угадали букву ;(')
    if count_mistakes < 9:
        print('Поздравляем, вы победили!')
    else:
        print('Вы проиграли ;(')