from bs4 import BeautifulSoup
import requests
import csv


def save():
    with open('toco_info.txt', 'a') as file:
        file.write(f"{comp['title']} -> Price: {comp['price']} -> Link^ {comp['link']}\n")

def parse():
    URL = 'https://www.technodom.kg/catalog/apple_smartphones'
    HEADERS = {
        'User-Agent' :	'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
    }

    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'tda-product-grid__item')
    comps = []


    for item in items:
        comps.append({
            'title': item.find('div', class_ = 'basetile__wrapper').get_text(strip = True),
            'price': item.find('div', class_ = 'basetile__price').get_text(strip = True),
            'link': URL + item.find('div', class_ = 'basetile__wrapper').find('a').get('href'),
        
        })
        global comp
        for comp in comps:
            print(f"{comp['title']} -> Price: {comp['price']} -> Link^ {comp['link']}")
            save()

parse()


def parser():
    PAGENATION = input("Введите количество страниц: ")
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        news_list = []
        for page in range(1, PAGENATION):
            print(f'Страница №{page} готова')
            html = get_html(URL, params={'page' : page})
            news_list.extend(get_content(html.text))
        news_save(news_list, CSV)
        print('Парсинг готов')
        # print(news_list)
    else:
        print('Error')

parser()

