from flask import request, redirect, render_template
from book_app import app
from book_app.models.author import Author
from book_app.models.book import Book


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
    author_favs = Author.get_author_details(author_id)
    return render_template('authorDetail.html', authorFavs = author_favs)

@app.route('/books')
def booksMain():
    return render_template("bookHome.html")

@app.route('/books/<int:book_id>')
def bookDetail(book_id):
    #same as author detail page but for the book
    pass