from bs4 import BeautifulSoup
import requests


def parse():
    url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Referer': 'localhost'
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")

    result = {}
    names = []

    name_block = soup.findAll('a', class_='ipc-title-link-wrapper')
    for data in name_block:
        parsed_name = data.h3.text
        names.append(parsed_name.split(" ", 1)[1].strip())

    rate_block = soup.findAll('span', class_='ratingGroup--imdb-rating')
    for i in range(len(rate_block)):
        result[names[i]] = float(rate_block[i].text[:3])

    print(result)
