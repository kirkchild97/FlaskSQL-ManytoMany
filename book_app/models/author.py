from book_app.config.mysqlconnection import connectToMySQL as sqlConnect
from book_app.models import book as getBook

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []

    @classmethod
    def save_author(cls, data):
        query = 'INSERT INTO authors (name, created_at, updated_at) VALUES(%(name)s, NOW(), NOW());'
        sqlConnect('books_and_authors').query_db(query, data)

    @classmethod
    def get_authors(cls):
        query = """SELECT id, name FROM authors;"""
        results = sqlConnect('books_and_authors').query_db(query)
        authors = []
        for author in results:
            authors.append(author)
        return authors

    @classmethod
    def get_author_details(cls, data):
        query = """SELECT id, name FROM authors
        WHERE id = %(id)s;"""
        results = sqlConnect('books_and_authors').query_db(query, data)
        authorInfo = results[0]
        query = """SELECT books.id, books.title, favorites.author_id FROM favorites
        LEFT JOIN books ON books.id = favorites.book_id WHERE favorites.author_id = %(id)s;"""
        results = sqlConnect('books_and_authors').query_db(query, data)
        print(f"Book Results: {results}")
        authorInfo['favorite_books'] = []
        for book in results:
            authorInfo['favorite_books'].append(book)
        results = getBook.Book.get_all_books()
        authorInfo['not_favorited'] = []
        for book in results:
            if len(authorInfo['favorite_books']) > 0:
                for favs in authorInfo['favorite_books']:
                    if book['id'] == favs['id']:
                        break
                    if favs == authorInfo['favorite_books'][len(authorInfo['favorite_books']) - 1]:
                        authorInfo['not_favorited'].append(book)
            else:
                authorInfo['not_favorited'].append(book)
        return authorInfo