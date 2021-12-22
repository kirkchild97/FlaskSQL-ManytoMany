from book_app.config.mysqlconnection import connectToMySQL as sqlConnect

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
    def get_author_details(cls, int:id):
        query = """SELECT authors.name, books.title FROM authors
        LEFT JOIN favorites ON authors.id = favorites.author_id
        LEFT JOIN books ON favorites.book_id = books.id
        WHERE authors.id = %(id)s;"""
        results = sqlConnect('books_and_authors').query_db(query, id)
        author_fav_books = []
        for favs in results:
            author_fav_books.append(favs)
        # print(f"Result: {author_fav_books}")
        return author_fav_books