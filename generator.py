import random


def generateString():

    generated_string = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSHTUVWXYZ'
    symbols_list = '!@#$%^&*()_+~/}{"?:><,.\\'
    alphabet_length = len(alphabet) - 1

    #generating random string with letters
    #_____________________________________

    for i in range(len(alphabet)):

        random_index = random.randint(0, alphabet_length)
        symbol = alphabet[random_index]
        if random.randint(0,1) == 0:
            symbol = symbol.lower()
        generated_string += symbol

    #generating random string including numbers
    #__________________________________________

    for i in range(len(generated_string)):

        string = ''

        random_value = str(random.randint(0,9))
        random_index = random.randint(0, len(generated_string)-1)

        generated_string = list(generated_string)
        generated_string.insert(random_index, random_value)

        for symbol in generated_string:
            string += symbol

    #generating random string including symbols
    #__________________________________________

    for i in range(len(string)):

        final_string = ''

        for symbol in symbols_list:
            random_value = random.randint(0, len(symbols_list)-1)
            random_symbol = symbols_list[random_value]

        random_index = random.randint(0, len(string)-1)

        string = list(generated_string)
        generated_string.insert(random_index, random_symbol)

        for symbol in generated_string:
            final_string += symbol

    return final_string

def main():

    generated_string = generateString()
    quarter = int(len(generated_string)*0.25-1)

    with open('password.txt', 'w') as password_file:
        password_file.write(generated_string[0:quarter])


main()