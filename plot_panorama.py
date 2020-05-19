import frequency, requests
from bs4 import BeautifulSoup


def today():
    text = ''
    home_url = 'https://panorama.pub'
    page = requests.get(home_url)
    unpretty_text = page.text
    soup = BeautifulSoup(unpretty_text, 'html.parser')
    for link in soup.find_all('a', rel = 'bookmark'):
        new_page_text = requests.get(link['href']).text
        new_soup = BeautifulSoup(new_page_text, 'html.parser')
        article = list(map(str, new_soup.findAll('p')))[2:-1]
        article = '\n'.join([i[3:-4] for i in article])
        text += ' ' + article
    return frequency.freq(text.split())
