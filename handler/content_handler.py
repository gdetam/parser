"""this is file handle content from content_parser.py."""

from bs4 import BeautifulSoup

from config import HOST

from model.book import Book


def get_count_pages(html):
    """Return the number of pages to process."""
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('a', class_='pn_button')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1


def get_content(html):
    """Collect content from the page for the specified classes."""
    soup = BeautifulSoup(html, 'html.parser')
    books = []
    for item in soup.find_all('div', class_='bookkitem'):
        books.append(Book(
            item.find('a', class_='bookkitem_name')
                .get_text(strip=True),

            item.find('div', class_='bookkitem_genre')
                .get_text(strip=True)
                .replace('\n', ''),

            item.find('span', class_='bookkitem_author')
                .get_text(strip=True)
                .replace('авторы', '')
                .replace('автор', '')
            if item.find('span', class_='bookkitem_author')
            else 'Автор неизвестен',

            item.find('div', class_='bookkitem_meta_block')
                .get_text(strip=True)
                .replace('Читает', '')
                .replace('Читают', '')
            if 'минут' not in item.find('div', class_='bookkitem_meta_block')
                                  .get_text(strip=True)
                                  .replace('Читает', '')
                                  .replace('Читают', '')
            else 'Исполнитель неизвестен',

            item.find('div', class_='bookkitem_about')
                .get_text(strip=True)
                .replace('\n', '')
                .replace('\r', '')
                .replace('/', '')
                .replace('а́', 'а')
                .replace('и́', 'и')
                .replace('о́', 'о'),

            HOST + item.find('a', class_='bookkitem_cover')
                       .get('href')
        ))

    return books
