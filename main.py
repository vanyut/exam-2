import requests
from bs4 import BeautifulSoup

def write_product_info(file, title, reviews, price):
    file.write(f"{title} | Reviews: {reviews} | Price: {price}\n")

def parse_category(url, discount=False):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all('div', class_='product-item')

    filename = 'all_products.txt' if not discount else 'discounted_products.txt'

    with open(filename, 'w', encoding='utf-8') as file:
        for product in products:
            title = product.find('div', class_='product-title').text.strip()
            reviews = product.find('span', class_='reviews-count').text.strip()
            price = product.find('span', class_='price').text.strip()

            if discount and product.find('span', class_='discount-percent'):
                write_product_info(file, title, reviews, price)
            elif not discount:
                write_product_info(file, title, reviews, price)

# Категорії без знижок
parse_category('https://allo.ua/ua/televizory/')
parse_category('https://allo.ua/ua/zarjadnye-stancii/')
parse_category('https://allo.ua/ua/products/mobile/')
parse_category('https://allo.ua/ua/products/internet-planshety/')
parse_category('https://allo.ua/ua/products/notebooks/')

# Категорії із знижками
parse_category('https://allo.ua/ua/televizory/', discount=True)
parse_category('https://allo.ua/ua/zarjadnye-stancii/', discount=True)
parse_category('https://allo.ua/ua/products/mobile/', discount=True)
parse_category('https://allo.ua/ua/products/internet-planshety/', discount=True)
parse_category('https://allo.ua/ua/products/notebooks/', discount=True)