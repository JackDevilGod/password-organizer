import secrets


class Password_generator:
    """class for generating passwords.
    """
    def __init__(self) -> None:
        """Initialise the password generator class.
        """
        default_types: tuple[str, ...] = tuple("letter (lowercase)")
        self._characters: dict[str, tuple[str, ...]] = self._generate_possible_character()
        self._character_types: tuple[tuple[str, bool], ...] = tuple([
            (_, _ in default_types) for _ in self._characters.keys()
            ])
        self._characters_selected: tuple[str, ...] = ()
        self._invalid_characters: set[str] = set()

        self.set_selected_characters_types(self.get_selected_characters_types())

    def get_blacklist(self) -> list[str]:
        """get a sorted list of black listed characters

        Returns:
            list[str]: list of character user added to black list
        """
        return sorted(list(self._invalid_characters))

    def add_to_blacklist(self, character: str) -> None:
        """Add user specified character to blacklist.

        Args:
            character (str): a string character use wants on the black list.

        Raises:
            ValueError: when the value is longer than one character.
        """
        if len(character) > 1:
            raise ValueError("has to be a one character")

        if character == "":
            return

        self._invalid_characters.add(character)

    def delete_from_blacklist(self, character: str) -> None:
        """Remove a character from the blacklist

        Args:
            character (str): single character string to be removed from blacklist
        """
        if character not in self._invalid_characters:
            return

        self._invalid_characters.remove(character)

    def get_character_types(self) -> tuple[str, ...]:
        """get all character type names without direct access.

        Returns:
            tuple[str, ...]: tuple of string that are the names of
            the type of character.
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
            character = self._characters_selected[secrets.randbelow(len(self._characters_selected))]

            while character in self._invalid_characters:
                character = self._characters_selected[secrets.randbelow(
                    len(self._characters_selected))]

            password += character

        return password


def main() -> None:
    test = Password_generator()
    types = test.get_character_types()
    type_selection: list[bool] = []

    for t in types:
        print(f"Would you like to include {t}. (Y/N)")
        answer = input().lower()

        while answer not in ["y", "n"]:
            print(f"Would you like to include {t}. (Y/N)")
            answer = input().lower()

        if answer == "y":
            type_selection.append(True)
        else:
            type_selection.append(False)

    print(f'Current blacklist: {test.get_blacklist()}')
    invalid_character = input("Input character to blacklist. (quit)\n")

    while invalid_character != "quit":
        try:
            test.add_to_blacklist(invalid_character)
            print(f"success added {invalid_character}")
        except ValueError:
            print("Invalid input has to be one character")

        print(f'Current blacklist: {test.get_blacklist()}')
        invalid_character = input("Input character to blacklist. (quit)\n")

    length: str = input("How long would you like the password?\n")

    while not length.isnumeric() and "." not in length and "," not in length:
        length = input("How long would you like the password?\n")

    test.set_selected_characters_types(tuple(type_selection))

    print(test.generate_password(int(length)))


if __name__ == "__main__":
    main()
