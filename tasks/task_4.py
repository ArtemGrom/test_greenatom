import requests


def get_ip(url: str) -> str:
    """Функция выводит текущий публичный IP-адрес компьютера"""
    page = requests.get(url)
    page.raise_for_status()
    return page.text


if __name__ == '__main__':
    url_address = 'https://ifconfig.me/'
    print(f'Текущий публичный IP-адрес компьютера - {get_ip(url_address)}')
