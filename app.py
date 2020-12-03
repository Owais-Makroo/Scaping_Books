from logging import debug
import requests
import logging

from pages.book_pages import BookPage


logging.basicConfig(format = '%(asctime)s %(levelname)-8s [%(filename)s : %(lineno)d] -> %(message)s',
                    datefmt = '%d-%m-%y : %H:%M:%S',
                    level = logging.DEBUG,
                    filename = 'log.txt'
)


logger = logging.getLogger('scraping')


logger.info('Loading the books list...')

page_content = requests.get(f'https://books.toscrape.com/').content
page = BookPage(page_content) 
books = page.book

for n in range(1, page.pages):
    page_content = requests.get(f'https://books.toscrape.com/catalogue/page-{n+1}.html').content
    page = BookPage(page_content) 
    books.extend(page.book)

print((len(books)))


