def str_is_valid(char):
    char = char.lower()
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    if((len(char) == 1) and (char in alphabet)):
        return True
    return False

if __name__ == '__main__':
    print('PyCharm')