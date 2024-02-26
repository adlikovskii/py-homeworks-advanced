import requests
from bs4 import BeautifulSoup
import json
keywords = ['Django', 'Flask']

url = ('https://spb.hh.ru/search/vacancy?area=1&area=2&'
       f'&text={"+".join(keywords)}&search_field=description')
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/58.0.3029.110 ',
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    vacancies = soup.find_all(class_='vacancy-serp-item__layout')
    results = []
    for vacancy in vacancies:
        link = vacancy.find('a', class_='bloko-link')['href']
        company = vacancy.find('a', class_='bloko-link bloko-link_kind-tertiary').text
        city = vacancy.find(attrs={"data-qa": "vacancy-serp__vacancy-address"}).text
        salary = vacancy.find(attrs={"data-qa": 'vacancy-serp__vacancy-compensation'})
        if salary:
            salary = salary.text
        else:
            salary = 'Не указана'

        vacancy_info = {
            'link': link,
            'company': company,
            'city': city,
            'salary': salary
            # Если нужен вывод без разделителей NNBSP и NBSP, можно добавить:
            # NNBSP - replace(u"\u202F", " ") или NBSP - replace(u'\xa0', ' ')
        }
        results.append(vacancy_info)

    with open('hh.json', 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=5)

    print('Парсинг завершен. Результаты сохранены в файле hh.json.')
else:
    print('Ошибка при выполнении запроса.')
