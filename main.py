import os

import requests
import argparse

from urllib.parse import urlparse
from urllib.parse import urlunparse
from dotenv import load_dotenv



def shorten_link(url, header):
    request_url = 'https://api-ssl.bitly.com/v4/shorten'
    request_body = {'long_url': url, 'domain': 'bit.ly'}
    response = requests.post(request_url, headers=header, json=request_body)
    response.raise_for_status()
    parsed_bitlink = urlparse(response.json()['link'])._replace(scheme='')
    bitlink = urlunparse(parsed_bitlink)[2:]
    return bitlink


def count_clicks(link, header):
    parsed_link = urlparse(link)
    if parsed_link.scheme:
        link = urlunparse(parsed_link._replace(scheme=''))[2:]
    request_url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary'
    response = requests.get(request_url, headers=header)
    response.raise_for_status()
    click_count = response.json()['total_clicks']
    return click_count


def is_bitlink(link, header):
    parsed_link = urlparse(link)
    if parsed_link.scheme:
        link = urlunparse(parsed_link._replace(scheme=''))[2:]
    request_url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}'
    response = requests.get(request_url, headers=header)
    return response.ok


def main():
    load_dotenv()
    bitly_token = os.getenv('BITLY_TOKEN')
    header = {
        'Authorization': f'Bearer {bitly_token}'
    }

    parser = argparse.ArgumentParser(description='Создание парсера, который собирает введенные в консоль данные')
    parser.add_argument('user_links', nargs='+', help='Введенные ссылки')
    args = parser.parse_args()
    
    for user_link in args.user_links:
        try:
            requests.get(user_link).raise_for_status()
        except requests.exceptions.HTTPError:
                print('Нерабочая ссылка - ', user_link)
                return

        if is_bitlink(user_link, header):
            clicks = count_clicks(user_link, header)
            print('Количество кликов ', clicks)
        else:
            bitlink = shorten_link(user_link, header)
            print('Битлинк ', bitlink)


if __name__ == '__main__':
    main()
