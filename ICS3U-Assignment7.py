# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: January 2023
# ICS3U-Assignment7.py File


def organize(first_list, second_list):
    final_list = []
    for counter in range(len(first_list) + len(second_list)):
        if counter < len(first_list):
            final_list.append(first_list[counter])
        if counter < len(second_list):
            final_list.append(second_list[counter])
    return final_list


def main():
    first_list = []
    second_list = []

    try:
        print('To end list enter "stop".')
        list_part = input("Input what you want to add to the first list: ")
        while list_part.upper() != "STOP":
            first_list.append(list_part)
            list_part = input("Input what you want to add to the first list: ")
        list_part = input("\nInput what you want to add to the second list: ")
        while list_part.upper() != "STOP":
            second_list.append(list_part)
            list_part = input("Input what you want to add to the second list: ")

        final_list = organize(first_list, second_list)

        print("\nThe organized list is {0}.".format(final_list))
        print("")

    except(ValueError):
        print("Invalid input, please try again.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
