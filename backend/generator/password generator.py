import secrets


class Password_generator:
    """class for generating passwords.
    """
    def __init__(self) -> None:
        """Initialise the password generator class.
        """
        self._characters: dict[str, tuple[str, ...]] = self._generate_possible_character()
        self._character_types: tuple[tuple[str, bool], ...] = tuple([
            (_, _ == "letter (lowercase)") for _ in self._characters.keys()
            ])
        self._characters_selected: tuple[str, ...] = self._characters["letter (lowercase)"]

    def get_character_types(self) -> tuple[str, ...]:
        """get all character type names without direct access.

        Returns:
            tuple[str, ...]: tuple of string that are the names of the type of character.
        """
        return tuple([_[0] for _ in self._character_types])

    def get_selected_characters_types(self) -> tuple[bool, ...]:
        """Get a tuple of character types that are included or not.

        Returns:
            tuple[bool, ...]: tuple of bool that represents if the character type is included
        """
        return tuple([_[1] for _ in self._character_types])

    def set_selected_characters_types(self, new_selected: tuple[bool, ...]) -> None:
        if len(new_selected) != len(self._character_types):
            raise ValueError("The amount selected and not do not match")

        self._character_types = tuple([(chr_type[0], stat)
                                      for chr_type, stat in zip(self._character_types, new_selected)
                                       ])

        new_selected_characters: list[str] = []

        for chr_type, selection in self._character_types:
            if selection:
                new_selected_characters += list(self._characters[chr_type])

        self._characters_selected = tuple(new_selected_characters)

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

    def generate_password(self, length: int) -> str:
        """generate password of given length with the preset character types selected.

        Args:
            length (int): length of password to generate.

        Returns:
            str: the password generated.
        """
        password: str = ""

        for _ in range(length):
            password += self._characters_selected[secrets.randbelow(len(self._characters_selected))]

        return password


def main() -> None:
    test = Password_generator()
    print(test.generate_password(20))
    x = test.get_character_types()

    test.set_selected_characters_types(tuple([True for _ in range(len(x))]))
    print(test.generate_password(20))


if __name__ == "__main__":
    main()
