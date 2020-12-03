import re
import logging
from bs4 import BeautifulSoup

from Locators.book_locator import BookCont
from Parser.book import BookParser

logger = logging.getLogger('scraping.book_pages')

class BookPage:
    def __init__(self, page) -> None:
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.parser = BeautifulSoup(page, 'html.parser')

    @property
    def book(self):
        logger.debug(f'Finding all books in the page using {BookCont.BOOK}')
        return [BookParser(e) for e in self.parser.select(BookCont.BOOK)]

    @property
    def pages(self):
        logger.debug('Finding all number of catalogue pages available.')
        locator = BookCont.PAGER
        no_pages = self.parser.select_one(locator).string
        logger.info(f'Found number of catalogue pages available: `{no_pages}`')
        pattern = '[0-9]+ of ([0-9]+)'
        no_of_pages = int(re.search(pattern, no_pages).group(1))
        logger.debug(f'Extracted number of pages as integer: `{no_of_pages}`')
        return no_of_pages
