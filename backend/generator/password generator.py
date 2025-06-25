import secrets


class Password_generator:
    """class for generating passwords.
    """
    def __init__(self) -> None:
        self._characters: dict[str, tuple[str, ...]] = self._generate_possible_character()
        self._character_names: tuple[str, ...] = tuple(self._characters.keys())

    @property
    def character_options(self):
        return self._character_names

    def _generate_possible_character(self) -> dict[str, tuple[str, ...]]:
        dictionary: dict[str, list[str]] = dict()

        dictionary["letter (lowercase)"] = [chr(_) for _ in range(97, 123)]
        dictionary["letter (uppercase)"] = [chr(_) for _ in range(65, 91)]
        dictionary["numbers"] = [str(_) for _ in range(10)]
        dictionary["punctuation"] = [".", "?", "'", '"', ",", "-", "—", "!", ":", ";", "(", ")",
                                     "[", "]", "/", "…"]
        dictionary["math expressions"] = ["+", "-", "*", "=", "%", "^"]
        dictionary["accented characters"] = ([chr(_) for _ in range(192, 215)] +
                                             [chr(_) for _ in range(216, 247)] +
                                             [chr(_) for _ in range(248, 256)])

        r_dictionary: dict[str, tuple[str, ...]] = dict()
        for key in dictionary.keys():
            r_dictionary[key] = tuple(dictionary[key])
        return r_dictionary


def generate_password_from_list(length: int,
                                possible_characters: list[str]) -> str:
    if length > 0 and len(possible_characters) == 0:
        raise ValueError("No available characters")
    password: str = ""
    list_length = len(possible_characters)

    for _ in range(length):
        password += possible_characters[secrets.randbelow(list_length)]

    return password


def main() -> None:
    pass


if __name__ == "__main__":
    main()
