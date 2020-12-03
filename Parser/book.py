import re
import logging

from Locators.book_properties_locator import BookProp


logger = logging.getLogger('scraping.book_parser')

class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }


    def __init__(self, parent) -> None:
        logger.debug(f'New book parser created...')
        self.parent = parent

    def __repr__(self) -> str:
        return f'<{self.title} costs {self.price} has {self.rating} stars>'

    @property
    def title(self):
        logger.debug('Finding book name...')
        locater = BookProp.TITLE_LOCATOR
        book_name = self.parent.select_one(locater).attrs['title']
        logger.debug(f'Found book name: `{book_name}')
        return book_name

    @property
    def link(self):
        logger.debug('Finding Book link...')
        locator = BookProp.LINK_LOCATOR
        book_link = self.parent.select_one(locator).attrs['href']
        logger.debug(f'Found book link: `{book_link}`')
        return book_link


    @property
    def price(self):
        logger.debug('Finding book price...')
        locater = BookProp.PRICE_LOCATOR
        price_with_extras = self.parent.select_one(locater).string

        exp = '£([0-9]+\\.[0-9]+)'
        price = float(re.search(exp, price_with_extras).group(1))
        logger.debug(f'Found book price: `{price}')
        return price

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BookProp.RATING_LOCATOR
        rating_item = self.parent.select_one(locator).attrs['class']
        rating_string = [a for a in rating_item if a != 'star-rating']
        logger.debug('Found book rating...')
        rating_number = BookParser.RATINGS.get(rating_string[0])
        logger.debug(f'Extracted book rating as integer: `{rating_number}')
        return rating_number

    


