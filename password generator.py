import random


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
    length: int = int(variable_input("num", "length of password"))
    password: str = ""

    for _ in range(length):
        password += chr(random.randint(33, 126))

    print(password)


if __name__ == "__main__":
    main()
