import collections
import SpanishDictParser


def main():
    print_logo_header()
    get_user_input(getting_user_intent())


def print_logo_header():
    print("************************************************")
    print("|                SPANISH DICTIONARY                 |")
    print("************************************************")


def get_user_input(option):
    print("What do you want to look up?")
    word = input("Word : ")
    url = SpanishDictParser.getting_url(word)
    phrase = SpanishDictParser.getting_basic_info(url, option)
    print(phrase)


def getting_user_intent():
    print("What do you want to do?")
    print("If you want to Define a selection press 1"
          "\nIf you want to Conjugate a word press 2")
    option = input("Choice : ")
    return int(option)


if __name__ == 'main':
    main()