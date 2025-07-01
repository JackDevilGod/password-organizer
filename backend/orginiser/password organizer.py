from function import remove_redundant_spaces, mergesort, standardize
import pandas as pd
from os import path


def main():
    """
    program that sorts your passwords based of website name
    :return: a sorted and organized wall of passwords
    """
    # create a list of passwords
    site_password_name: str = input()

    password_list: list[list[str]] = []
    while site_password_name != "":
        password_list.append(site_password_name.split("\t"))
        site_password_name = input()

    # remove redundant spaces
    trimmed_password_list = remove_redundant_spaces(password_list)

    # sort list
    sorted_password_list = mergesort(trimmed_password_list)

    # standardize size of website name, password
    standardized_password_list = standardize(sorted_password_list)

    # print the sorted password list
    # for line in standardized_password_list:
    #     print("\t".join(line))

    table = pd.DataFrame(standardized_password_list, columns=["website",
                                                              "password",
                                                              "username"])
    print(table)
    save_path = path.split(__file__)[0]
    print(save_path)

    table.to_csv(path.join(save_path, "export.csv"),
                 index=False,
                 sep="\t")


if __name__ == "__main__":
    main()
