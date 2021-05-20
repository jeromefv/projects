import string

lower_letters = string.ascii_lowercase

missing_letters = []

all_letters_flag = False

while not all_letters_flag:
    test = input('Type in a sentence using all 26 letters of the alphabet: ')
    for letter in lower_letters:
        if letter in test:
            pass
        else:
            missing_letters.append(letter)
    if len(missing_letters) != 0:
        print(f'The letters {missing_letters} are missing from your sentence.')
        missing_letters = []
    else:
        all_letters_flag = True
        print(f'The sentence "{test}" has all 26 letters of the alphabet.')
