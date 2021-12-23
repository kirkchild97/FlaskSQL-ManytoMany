from book_app.config.mysqlconnection import connectToMySQL as sqlConnect
from book_app.models import author as getAuthor

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors_favorited = []

    @classmethod
    def get_all_books(cls):
        query = """SELECT id, title, num_of_pages FROM books;"""
        results = sqlConnect('books_and_authors').query_db(query)
        all_books = []
        for book in results:
            all_books.append(book)
        return all_books

    @classmethod
    def get_book_details(cls, data):
        query = """SELECT id, title, num_of_pages FROM books
        WHERE id = %(book_id)s;"""
        results = sqlConnect('books_and_authors').query_db(query, data)
        bookInfo = results[0]
        query = """SELECT authors.id, authors.name, favorites.book_id FROM favorites
        LEFT JOIN authors ON authors.id = favorites.author_id WHERE favorites.book_id = %(book_id)s;"""
        results = sqlConnect('books_and_authors').query_db(query, data)
        print(f"Book Results: {results}")
        bookInfo['favorite_authors'] = []
        for author in results:
            bookInfo['favorite_authors'].append(author)
        results = getAuthor.Author.get_authors()
        bookInfo['not_favorited'] = []
        for author in results:
            if len(bookInfo['favorite_authors']) > 0:
                for favs in bookInfo['favorite_authors']:
                    if author['id'] == favs['id']:
                        break
                    if favs == bookInfo['favorite_authors'][len(bookInfo['favorite_authors']) - 1]:
                        bookInfo['not_favorited'].append(author)
            else:
                bookInfo['not_favorited'].append(author)
        return bookInfo

    @classmethod
    def save_book(cls, data):
        query = """INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES(%(title)s, %(num_of_pages)s, NOW(), NOW());"""
        sqlConnect('books_and_authors').query_db(query, data)
