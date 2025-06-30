def who_goes_first(first_word: str, second_word: str) -> int:
    """
    function that gives back an int that represents if the first word should go first
    :param first_word:
    :param second_word:
    :return:
    """
    if first_word[0] == second_word[0]:
        length_first_word = len(first_word)
        length_second_word = len(second_word)

        if length_first_word > 1 and length_second_word > 1:
            who_goes_first(first_word[1:], second_word[1:])
        elif length_first_word > length_second_word:
            return 1
        elif length_first_word < length_second_word:
            return 2
        else:
            return 0
    elif first_word[0] > second_word[0]:
        return 2
    else:
        return 1

    return 1


def mergesort(password_list: list[list[str]]) -> list[list[str]]:
    """
    uses merge sort to sort the list based of website name
    :param password_list:
    :return:
    """
    srtlst: list = []
    length: int = len(password_list)
    if length == 1:
        return password_list
    else:
        half: int = length // 2
        first, second = mergesort(password_list[:half]), mergesort(password_list[half:])
        length_first: int = len(first)
        length_second: int = len(second)

        index_first: int = 0
        index_second: int = 0
        while index_second < length_second or index_first < length_first:
            if index_first >= length_first:
                srtlst += second[index_second:]
                break
            elif index_second >= length_second:
                srtlst += first[index_first:]
                break

            value_first = first[index_first][0].lower()
            value_second = second[index_second][0].lower()
            sort_state = who_goes_first(value_first, value_second)

            if sort_state == 1:
                srtlst.append(first[index_first])
                index_first += 1
            elif sort_state == 2:
                srtlst.append(second[index_second])
                index_second += 1
            else:
                srtlst.append(first[index_first])
                srtlst.append(second[index_second])
                index_first += 1
                index_second += 1
        return srtlst


def remove_redundant_spaces(password_list: list[list[str]]) -> list[list[str]]:
    """
    removes redundant spaces in front and back of website name, password and username
    :param password_list:
    :return: the password list with no redundant spaces
    """
    for line_index in range(0, len(password_list)):
        password_list[line_index][0] = password_list[line_index][0].strip()
        password_list[line_index][1] = password_list[line_index][1].strip()
        if len(password_list[line_index]) >= 3:
            password_list[line_index][2] = password_list[line_index][2].strip()

    return password_list


def standardize(sorted_password_list: list[list[str]]) -> list[list[str]]:
    """
    adds redundant spaces to the back of website names and password to standardize their size
    :param sorted_password_list:
    :return: standardized_sorted_password_list
    """
    # get max length of website name and password
    max_length_website: int = 0
    max_length_password: int = 0
    for line in sorted_password_list:
        website_length: int = len(line[0])
        password_length: int = len(line[1])

        if website_length > max_length_website:
            max_length_website = website_length
        if password_length > max_length_password:
            max_length_password = password_length

    # add spaces
    for line_index in range(0, len(sorted_password_list)):
        sorted_password_list[line_index][0] = (sorted_password_list[line_index][0] +
                                               (" " * (max_length_website - len(sorted_password_list[line_index][0]))))
        sorted_password_list[line_index][1] = (sorted_password_list[line_index][1] +
                                               (" " * (max_length_password - len(sorted_password_list[line_index][1]))))

    return sorted_password_list

def main():
    return


if __name__ == "__main__":
    main()
