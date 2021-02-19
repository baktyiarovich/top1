import requests
from bs4 import BeautifulSoup


URL = 'https://auto.ria.com/newauto/actions/marka-mercedes-benz/model-vito-pass/'
HEADERS = {
    'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/64.0', 
    }

def get_html(url, params=None):
    r = requests.get(url, headers = HEADERS, params=params)
    return rin send
    r = adapter.send(request, **kwargs)


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'proposition  ')

def parse():
    html = get_html(URL)
    if html.stqtus_code == 200:
        print(html.text)
    else:
        print("error")

parse()
