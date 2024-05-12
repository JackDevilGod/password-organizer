import secrets


def variable_input(var_type: str, texts=""):
    """
    function to get the correct input
    :param var_type:
    :param texts:
    :return:
    """
    in_texts = texts + "\n"
    var = input(in_texts)

    match var_type:
        case "num":
            while not var.isnumeric():
                var = input(in_texts)

        case "alpha":
            while not var.isalpha():
                var = input(in_texts)

    return var


def main():
    password: str = ""

    # settings
    length: int = 20
    symbols: bool = True
    upper_letters: bool = True
    lower_letters: bool = True
    numbers: bool = True

    symbol_list: list[int] = ([_ for _ in range(33, 47)] + [_ for _ in range(58, 65)] +
                              [_ for _ in range(91, 97)] + [_ for _ in range(123, 127)])
    upper_letters_list: list[int] = [_ for _ in range(65, 91)]
    lower_letter_list: list[int] = [_ for _ in range(97, 123)]
    numbers_list: list[int] = [_ for _ in range(48, 58)]

    possible_list: list[int] = list()

    if symbols:
        possible_list += symbol_list
    if upper_letters:
        possible_list += upper_letters_list
    if lower_letters:
        possible_list += lower_letter_list
    if numbers:
        possible_list += numbers_list

    for _ in range(length):
        password += chr(possible_list[secrets.randbelow(len(possible_list))])

    print(password)


if __name__ == "__main__":
    main()
