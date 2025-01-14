import os
import mysql.connector

db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    user=os.getenv("MYSQL_USER", "testuser"),
    password=os.getenv("MYSQL_PASSWORD", "testpassword"),
    database=os.getenv("MYSQL_DATABASE", "testdb"),
    port=3306
)
