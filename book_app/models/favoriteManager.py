from book_app.config.mysqlconnection import connectToMySQL as sqlConnect

class Favorite:
    def __init__(self, data):
        self.book_id = data['book_id']
        self.author_id = data['author_id']

    @classmethod
    def setFavorite(cls, data):
        query = """INSERT INTO favorites (book_id, author_id) VALUES(%(book_id)s, %(author_id)s);"""
        sqlConnect('books_and_authors').query_db(query, data)