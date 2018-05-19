import SpanishDictParser
from os import system
from time import sleep


def main():
    print_logo()
    to_do = what_to_do()

    phrase = input("\nWhat do you want to translate : ")

    if to_do == 1:
        case_of_conjugation(word=phrase)
    elif to_do == 2:
        case_of_translation(phrase=phrase)
    elif to_do == 3:
        case_of_lookup(phrase=phrase)

    stop_or_not()


def print_logo():
    print('*******************************************')
    print('|       SPANISH DICTIONARY PARSER          |')
    print('*******************************************')


def stop_or_not():
    choice = None
    while choice != 'n':
        print('\nDo you want to look something else up?')
        choice = input('Choice [Y] or [N] : ')
        choice = choice.lower().strip()

        if choice == 'y':
            system('cls')
            main()
        elif choice == 'n':
            system('cls')
            print('Goodbye!')
            sleep(1)
            exit()
        elif choice != 'y' and choice != 'n':
            print('Sorry, I did not understand "{0}", could you try again...'.format(choice))


def what_to_do():
    choice = None
    while choice != '1' or choice != '2' or choice != '3':
        print('\nWhat do you want me to do?')
        print('[1] Conjugate'
              '\n[2] Translate'
              '\n[3] Look up')
        choice = input('Choice : ')
        choice = choice.lower().strip()

        if choice == '1':
            return 1
        elif choice == '2':
            return 2
        elif choice == '3':
            return 3
        else:
            print('Sorry I did not understand "{0}", please try again'.format(choice))


def case_of_conjugation(word):
    print(SpanishDictParser.checking_word_for_conjugation(word=word))


def case_of_translation(phrase):
    print(SpanishDictParser.checking_phrase_for_translation(phrase=phrase))


def case_of_lookup(phrase):
    print(SpanishDictParser.looking_up(phrase=phrase))


if __name__ == '__main__':
    main()
