"""this is file parse content from web site."""

from config import HEADERS, PATH

from content_saver import save_to_file

from handler.content_handler import get_content, get_count_pages

import requests


def parse():
    """Loop through urls, collect content and save to file."""
    all_books = []
    urls = __get_urls()
    for url in urls:
        all_books.extend(__parse_by_url(url))
    save_to_file(all_books)


def __get_urls():
    """Read the urls.txt file and creates urls_list from it."""
    urls_list = []
    with open(PATH, 'r') as urls:
        for url in urls.readlines():
            url = url.strip()
            urls_list.append(url)
        return urls_list


def __get_html(url: str, params=None):
    """Process url and provides html on it."""
    r = requests.get(url, headers=HEADERS, params=params)
    r.encoding = 'utf-8'
    return r


def __parse_by_url(url: str):
    """Gathers content from a page using html from __get_html (url)."""
    all_books = []
    html = __get_html(url)
    if html.status_code == 200:
        count_pages = get_count_pages(html.text)
        for page in range(1, count_pages + 1):
            print(f'Парсинг страницы {page} из {count_pages}')
            html = __get_html(url, params={'page': page})
            all_books.extend(get_content(html.text))
        print(all_books)
        print(f'Получено книг: {len(all_books)}')
    else:
        print('Error')
    return all_books
