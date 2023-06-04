import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

url = 'https://zoro.to/most-popular'
payloads = {'page': 1}
file = open('zoro_to.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['anime title', 'number of episodes'])

while payloads['page'] < 6:
    response = requests.get(url, params=payloads)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    small_soup = soup.find('div', class_='film_list-wrap')
    all_anime = small_soup.find_all('div', class_='flw-item')

    for anime in all_anime:
        title = anime.h3.a.text
        number_of_eps = anime.find('div', class_='tick-item tick-sub').text
        print(title, number_of_eps)
        csv_obj.writerow([title, number_of_eps])
    payloads['page'] += 1
    sleep(randint(15, 20))
