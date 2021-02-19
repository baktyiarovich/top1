from bs4 import BeautifulSoup
import requests
import csv

CSV = 'minfin_com_ua_deposits.csv'
HOST = 'https://minfin.com.ua'
URL = 'https://minfin.com.ua/cards/'
HEADERS = {
    'Accept' : 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',    
    'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/64.0'
}

def get_html(url, params=''):
    r = requests.get(url, headers = HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('div', class_ = 'product-item')
    news_list = []

    for item in items:
        news_list.append({
            'date': item.find('div', class_ = 'title').get_text(strip = True),
            'title' : item.find('div', class_ = 'brand').get_text(strip = True),
            'link' : item.find('div', class_ = 'title').find('a').get('href'),
            'img' : item.find('div', class_ = 'image').find('img').get('src'),
        })
    return news_list

html = get_html(URL)
print(get_content(html.text))

# def news_save(items, path):
#     with open(path, 'a') as file:
#         writer = csv.writer(file, delimiter=';')
#         writer.writerow(['День публикации', 'Новость', 'Ссылка'])
#         for item in items:
#             writer.writerow([item['date'], item['title'], item['link']])

# def parser():
#     PAGENATION = input("Введите количество страниц: ")
#     PAGENATION = int(PAGENATION.strip())
#     html = get_html(URL)
#     if html.status_code == 200:
#         news_list = []
#         for page in range(1, PAGENATION):
#             print(f'Страница №{page} готова')
#             html = get_html(URL, params={'page' : page})
#             news_list.extend(get_content(html.text))
#         news_save(news_list, CSV)
#         print('Парсинг готов')
#         # print(news_list)
#     else:
#         print('Error')

# parser()