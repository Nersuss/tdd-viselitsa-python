def str_is_valid(char):
    char = char.lower()
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    if((len(char) == 1) and (char in alphabet)):
        return True
    return False

def load_words(path):
    with open(path, 'r', encoding="utf-8") as file:
        return [row.strip() for row in file]

words = load_words('words.txt')

if __name__ == '__main__':
    print('Игра Виселица началась!')
    print('Введите букву:')
