import logging

from app import books

logger = logging.getLogger('scraping.menu')

USER_CHOICE = '''Choose on of the following:

- 'b' to look at 5 star books
- 'c' to look at cheapest books
- 'n' to look a next book in the catalogue
- 'q' to quit

Enter your choice: '''



def get_top_rated_books():
    logger.info('Finding books by rating...')
    top_rated_books = [book for book in books if book.rating == 5][:5]
    for book in top_rated_books:
        print(book)
    logger.info('Printed books by rating...')


def get_cheapest_books():
    logger.info('Finding books by price...')
    cheapest_books = sorted(books, key = lambda x: x.price)[:5]
    for book in cheapest_books:
        print(book)
    logger.info('Printed books by price...')

def get_top_rated_books_by_price():
    top_books_by_price = sorted(books, key = lambda x:(x.rating*-1, x.price))[:10]
    for book in top_books_by_price:
        print(book)


books_generator = (x for x in books)

def get_next_book():
    logger.info('Getting next book from generator of all books...')
    print(next(books_generator))
    logger.info('Printed next book...')





USER_OPTIONS = {
    'b': get_top_rated_books,
    'c': get_cheapest_books,
    'n': get_next_book,
    
}

def user_menu():
    selection = input(USER_CHOICE)
    while selection != 'q':
        if selection in USER_OPTIONS:
            USER_OPTIONS[selection]()
        else:
            print("\n\n--Please choose a valid option..!--\n\n")
        selection = input(USER_CHOICE)
    logger.info('Terminating program...')


user_menu()
