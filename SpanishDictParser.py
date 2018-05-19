import requests
import bs4
import collections


def checking_word_for_conjugation(word):
    """
    This method gets and searches for definition and conjugation of the given word on SpanishDict
    :param word: word that user want to be conjugated
    :return: returns the definition and conjugation  of the given word
    """

    # TODO: add the ability to print out basic conjugations for the word

    url = 'http://www.spanishdict.com/conjugate/{0}'.format(word)
    url_return = requests.get(url=url)
    url_return = url_return.text

    soup = bs4.BeautifulSoup(url_return, "html.parser")

    """
    This part does Error Handling.
    In case there is no conjugation for the word, 
    or the word fits in a different category 
    this section will try to figure out what to do to get the best result
    """

    # TODO: add redirects to other types in case this one result's in error

    try:
        word_definition = soup.find(class_='el').get_text()
    except AttributeError:
        return 'ERROR'
    else:
        return text_clean_up(word_definition)


def checking_phrase_for_translation(phrase):
    """
    This method checks for translation of the given phrase and returns it to the user
    :param phrase: Phrase that needs to be translated
    :return: Returns the translation of the given phrase of an error
    """

    url = 'http://www.spanishdict.com/translate/{0}'.format(phrase)
    url_return = requests.get(url=url)
    url_return = url_return.text

    soup = bs4.BeautifulSoup(url_return, "html.parser")
    """
    This part does Error Handling.
    In case the phrase or word fits in a different category or web page redirects it,
    this part will handle these possible errors 
    """

    # TODO: add redirects to other types in case this one result's in error

    if translation_error_handler(phrase=phrase) == '1':
        try:
            phrase_translation = soup.find(class_='el').get_text()
        except AttributeError:
            return 'ERROR'
        else:
            return text_clean_up(phrase_translation)


def translation_error_handler(phrase):
    url = 'http://www.spanishdict.com/translate/{0}'.format(phrase)
    url_return = requests.get(url=url)
    url_return = url_return.text

    soup = bs4.BeautifulSoup(url_return, "html.parser")
    try:
        phrase_translation = soup.find(class_='spelling-row').get_text()
    except AttributeError:
        return '1'

    else:
        if phrase_translation == "We couldn't find what you were looking for.":
            return '{0} does not exist, try again'.format(phrase)


def text_clean_up(text: str):
    """
    This method cleans up the text which was scraped from web page by removing whitespaces
    :param text: The input text
    :return: Cleaned-up output text
    """

    if not text:
        return text

    text = text.strip()
    return text
