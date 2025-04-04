import main

def test_str_is_valid():
    assert main.str_is_valid('б') == True
    assert main.str_is_valid('К') == True
    assert main.str_is_valid('гт') == False
    assert main.str_is_valid('к1') == False
    assert main.str_is_valid('щщ') == False
    assert main.str_is_valid('s') == False
    assert main.str_is_valid('W') == False
    assert main.str_is_valid('2') == False
    assert main.str_is_valid('') == False
    assert main.str_is_valid('%') == False

def test_load_words():
    assert main.load_words('words.txt') != None
    assert main.load_words('words.txt') != []