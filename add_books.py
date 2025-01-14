import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your actual username
    password="1234",  # Replace with your actual password
    database="nbl_bookstore"
)

def add_books():
    books = [
        {"title": "Python Programming", "category": "technology", "publication_date": "2023-08-01"},
        {"title": "History of China", "category": "history", "publication_date": "2023-07-19"},
        {"title": "Economic Theory", "category": "economy", "publication_date": "2023-06-25"},
        {"title": "Tourism in Europe", "category": "tourism", "publication_date": "2023-05-12"},
        {"title": "Early Readers - Fairy Tales", "category": "early_readers", "publication_date": "2023-04-10"},
    ]

    cursor = db.cursor()
    for book in books:
        cursor.execute(
            "INSERT INTO books (title, category, publication_date) VALUES (%s, %s, %s)",
            (book['title'], book['category'], book['publication_date'])
        )
    db.commit()
    cursor.close()

if __name__ == '__main__':
    add_books()
