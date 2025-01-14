from flask import Flask, jsonify, render_template, request, url_for
from datetime import datetime
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your actual username
    password="1234",  # Replace with your actual password
    database="nbl_bookstore"
)

@app.route('/books', methods=['GET'])
def get_books():
    category = request.args.get('category')
    search_query = request.args.get('q')
    cursor = db.cursor(dictionary=True)
    
    if search_query:
        cursor.execute("SELECT * FROM books WHERE title LIKE %s", ('%' + search_query + '%',))
    elif category:
        cursor.execute("SELECT * FROM books WHERE category = %s", (category,))
    else:
        cursor.execute("SELECT * FROM books")
        
    books = cursor.fetchall()
    cursor.close()
    return jsonify(books)

@app.route('/books/<int:book_id>')
def book_detail(book_id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    book = cursor.fetchone()
    cursor.close()
    return render_template('detail.html', book=book)

@app.route('/new-books', methods=['GET'])
def new_books():
    current_month = datetime.now().strftime("%Y-%m")
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books WHERE DATE_FORMAT(publication_date, '%Y-%m') = %s", (current_month,))
    new_books = cursor.fetchall()
    cursor.close()
    return jsonify(new_books)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
