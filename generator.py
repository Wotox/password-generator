import secrets


def generateString():

    generated_string = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSHTUVWXYZ'
    symbols_list = '!@#$%^&*()_+~/}{"?:><,.\\'
    alphabet_length = len(alphabet) - 1

    #generating random string with letters
    #_____________________________________

    step = 0
    while step <= len(alphabet):

        random_index = secrets.randbelow(alphabet_length)
        symbol = alphabet[random_index]
        
        if secrets.randbelow(1) == 0:
            symbol = symbol.lower()

        generated_string += symbol
        step += 1

    #generating random string including numbers
    #__________________________________________

    step = 0
    while step <= len(alphabet):

        string = ''

        random_value = str(secrets.randbelow(9))
        random_index = secrets.randbelow(len(generated_string)-1)

        generated_string = list(generated_string)
        generated_string.insert(random_index, random_value)

        for symbol in generated_string:
            string += symbol
        step += 1

    #generating random string including symbols
    #__________________________________________

    step = 0
    while step <= len(alphabet):

        final_string = ''

        for symbol in symbols_list:
            random_value = secrets.randbelow(len(symbols_list)-1)
            random_symbol = symbols_list[random_value]

        random_index = secrets.randbelow(len(string)-1)

        string = list(generated_string)
        generated_string.insert(random_index, random_symbol)

        for symbol in generated_string:
            final_string += symbol
        step += 1

    return final_string

def main():

    generated_string = generateString()
    quarter = int(len(generated_string)*0.25-1)

    with open('password.txt', 'w') as password_file:
        password_file.write(generated_string[0:quarter])


main()