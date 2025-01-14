import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="nbl_bookstore"
)

def add_monthly_books():
    current_month = datetime.now().strftime("%Y-%m")
    books = [
        {"title": f"New Book {current_month} - 1", "category": "history", "publication_date": f"{current_month}-11"},
        {"title": f"New Book {current_month} - 2", "category": "economy", "publication_date": f"{current_month}-11"},
        {"title": f"New Book {current_month} - 3", "category": "tourism", "publication_date": f"{current_month}-11"},
        # 添加更多书籍条目
    ]

    cursor = db.cursor()
    for book in books:
        cursor.execute("INSERT INTO books (title, category, publication_date) VALUES (%s, %s, %s)",
                       (book['title'], book['category'], book['publication_date']))
    db.commit()
    cursor.close()

if __name__ == '__main__':
    add_monthly_books()
