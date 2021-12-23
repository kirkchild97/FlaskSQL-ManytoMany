from flask import request, redirect, render_template
from book_app import app
from book_app.models.author import Author
from book_app.models.book import Book
from book_app.models.favoriteManager import Favorite as Fav


@app.route('/')
def sendHome():
    return redirect('/authors')

@app.route('/authors')
def authorsMain():
    authors = Author.get_authors()
    return render_template("authorHome.html", authors = authors)

@app.route('/authors/createNew', methods = ['POST'])
def createAuthor():
    data = {
        'name' : request.form['name']
    }
    Author.save_author(data)
    return redirect('/authors')

@app.route('/authors/<author_id>')
def authorDetail(author_id):
    data = { 'id' : int(author_id) }
    author_favs = Author.get_author_details(data)
    print(author_favs)
    return render_template('authorDetail.html', authorFavs = author_favs, id = author_id)

@app.route('/authors/<author_id>/addFav', methods=['POST'])
def addFavorites(author_id):
    data = {
        'book_id' : request.form['title'],
        'author_id' : author_id
    }
    Fav.setFavorite(data)
    return redirect(f'/authors/{author_id}')

@app.route('/books')
def booksMain():
    all_books = Book.get_all_books()
    return render_template("bookHome.html", books = all_books)

@app.route('/books/createNew', methods = ['POST'])
def save_book():
    data = {
        'title' : request.form['title'],
        'num_of_pages' : request.form['num_of_pages']
    }
    Book.save_book(data)
    return redirect('/books')

@app.route('/books/<int:book_id>')
def bookDetail(book_id):
    
    render_template('bookDetail.html')

@app.route('/books/<int:book_id>/addFav')
def bookAddFavorites(book_id):
    data = {
        'book_id' : book_id,
        'author_id' : request.form['name']
    }
    Fav.setFavorite(data)
    return redirect(f'/books/{book_id}')