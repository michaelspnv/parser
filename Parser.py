from bs4 import BeautifulSoup
import requests
import openpyxl


def parse():
    url = 'https://omsk.cian.ru/kupit-kvartiru/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Referer': 'localhost'
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")

    data = soup.findAll('div', class_='_93444fe79c--link--DqDOy')
    prices = soup.findAll('span', class_='_93444fe79c--color_black_100--Ephi7 _93444fe79c--lineHeight_28px--KFXmc '
                                         '_93444fe79c--fontWeight_bold--BbhnX _93444fe79c--fontSize_22px--sFuaL '
                                         '_93444fe79c--display_block--KYb25 _93444fe79c--text--e4SBY '
                                         '_93444fe79c--text_letterSpacing__normal--tfToq')

    result = []

    for i in range(len(data)):
        current = []
        current.append(data[i].div.a.span.span.text)
        if data[i].div.a.div:
            current.append(data[i].div.a.div.span.text)
        else:
            current.append('-')
        current.append(prices[i].text)

        result.append(current)

    return result


def write_to_excel(data):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(['Текст объявления', 'Информация о квартире', 'Цена'])

    for item in data:
        sheet.append(item)

    workbook.save('cian-info.xlsx')
    print('Данные успешно записаны в файл cian-info.xlsx')
