import requests
import os
from urllib.parse import urlparse
from urllib.parse import urlunparse
from dotenv import load_dotenv
import argparse



def shorten_link(url, header):
    request_url = 'https://api-ssl.bitly.com/v4/shorten'
    request_body = {'long_url': url, 'domain': 'bit.ly'}
    response = requests.post(request_url, headers=header, json=request_body)
    response.raise_for_status()
    parsed_bitlink = urlparse(response.json()['link'])._replace(scheme='')
    bitlink = urlunparse(parsed_bitlink).replace('//', '')
    return bitlink


def count_clicks(link, header):
    link = urlunparse(urlparse(link)._replace(scheme='')).replace('//', '')
    request_url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary'
    response = requests.get(request_url, headers=header)
    response.raise_for_status()
    click_count = response.json()['total_clicks']
    return click_count


def is_bitlink(link, header):
    link = urlunparse(urlparse(link)._replace(scheme='')).replace('//', '')
    request_url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}'
    response = requests.get(request_url, headers=header)
    return response.ok


def main():
    load_dotenv()
    bitly_token = os.getenv('BITLY_TOKEN')
    header = {
        'Authorization': f'Bearer {bitly_token}'
    }

    parser = argparse.ArgumentParser(description='Сохраняет переданные в консоль URL адреса')
    parser.add_argument('user_links', nargs='+', help='Введенные ссылки')
    args = parser.parse_args()
    
    for user_links in args.user_links:
        try:
            requests.get(user_links).raise_for_status()
        except requests.exceptions.HTTPError:
                print('Нерабочая ссылка')
                return

        if is_bitlink(user_links, header):
            clicks = count_clicks(user_links, header)
            print('Количество кликов ', clicks)
        else:
            bitlink = shorten_link(user_links, header)
            print('Битлинк ', bitlink)


if __name__ == '__main__':
    main()
