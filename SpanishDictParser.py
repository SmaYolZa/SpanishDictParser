import requests
import bs4
import collections


def getting_url(word):
    url = 'http://www.spanishdict.com/conjugate/{0}'.format(word)
    response = requests.get(url=url)
    return response.text


def getting_basic_info(html, option):
    soup = bs4.BeautifulSoup(html, "html.parser")
    if option == 1 and (soup.find(class_='el') != 'NoneType'):
        definition = soup.find(class_='el').get_text()
    elif option == 2 and (soup.find(class_='el') != 'NoneType'):
        definition = soup.find(class_='el').get_text()
        conjugation = None
    else:
        return 'ERROR'
    return definition