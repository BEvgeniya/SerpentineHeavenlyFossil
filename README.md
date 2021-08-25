# SerpentineHeavenlyFossil

Программа на основе [Bitly Api](https://dev.bitly.com/ "Bitly Api") для сокращения ссылок
 и подсчета переходов по сокращенной ссылке.

## Environment

### Requirements

Требует Python 3.0+ компилятор и установку библиотек:
1) requests
2) python-dotenv
А также токен Bitly API

```bash
pip install requests
pip install python-dotenv
```

### Environment variables

- BITLY_TOKEN
 
#### How to get

Зарегистрируйтесь на [bitly api](https://dev.bitly.com/ "bitly api") и получите уникальный api-ключ


## Run

Запускается на Linux(Python 3) или Windows:

```bash

 python main.py

```

После запуска программы введите url-адрес для получения сокращенной ссылки на него,
либо введите битлинк (ранее сокращенную ссылку) для получения количества переходов по нему.
Допускается введение от 1 и более ссылок одновременно.

## Notes

Подробнее о работе программы:

**def shorten_link(url, header)**
Принимает на вход адрес страницы, который нужно сократить,
 и словарь заголовков (нужен для авторизации в Bitly).
Осуществляет запрос к API и возвращает битлинк - краткую ссылку.

**def count_clicks(link, header)**
Принимает на вход битлинк и словарь заголовков. 
 Осуществляет запрос к API и возвращает количество переходов по битлинку.
 
**def is_bitlink(link, header)**
Принимает на вход адрес страницы и словарь заголовков. 
Проверяет, обращаясь к API, является ли переданная ссылка битлинком.
Возвращает True или False значение в зависимости от того, 
является ли переданная ссылка битлинком.
Данная функция нужна для того, чтобы распознать битлинк
 и вызвать функцию подсчета кликов
  (или функцию сокращения ссылки, если передан обычный url)


