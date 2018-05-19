import requests
import bs4
import collections


def getting_url(word):
    url = 'http://www.spanishdict.com/conjugate/{0}'.format(word)
    response = requests.get(url=url)
    return response.text


def getting_basic_info(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    definition = soup.find(class_='el').get_text()
    return definition