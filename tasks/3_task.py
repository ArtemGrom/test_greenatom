import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent


def get_page_html(url: str) -> object:
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    page_html = BS(response.text, 'html.parser')
    return page_html


def count_all_tag(page: object) -> int:
    count = 0
    for _ in page.findAll():
        count += 1
    return count


def count_tag_with_attrs(page: object, count: int = 0) -> int:
    if page.name:
        if page.attrs:
            count += 1
        for child in page.children:
            count = count_tag_with_attrs(child, count)
    return count


if __name__ == '__main__':
    url = 'https://greenatom.ru/'
    get_html = get_page_html(url)
    print(f'Количество всех html-тегов на странице {url} - {count_all_tag(get_html)}')
    print(f'Количество html-тегов с атрибутами на странице {url} - {count_tag_with_attrs(get_html)}')

