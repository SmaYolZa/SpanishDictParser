import SpanishDictParser
from os import system
from time import sleep


def main():
    print_logo()
    word = input("What do you want to translate : ")
    url = SpanishDictParser.getting_url(word)
    print(SpanishDictParser.getting_basic_info(url))
    what_to_do_next()


def print_logo():
    print('*******************************************')
    print('|       SPANISH DICTIONARY PARSER          |')
    print('*******************************************')


def what_to_do_next():
    print('Do you want to look something else up?')
    choice = input('Choice [Y] or [N] : ')
    choice.islower()
    if choice == 'y':
        system('cls')
        main()
    elif choice == 'n':
        print('Goodbye!')
        sleep(1)
        exit()


if __name__ == '__main__':
    main()