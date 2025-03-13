from flask import Flask, render_template
import mysql.connector
import os

config = {
    'user': 'wbsadmin',  # Nazwa użytkownika bazy danych
    'password': 'Testowe7',  # Hasło użytkownika
    'host': 'wbspython2025.mysql.database.azure.com',  # Nazwa serwera Azure MySQL
    'database': 'wbspython2025',  # Nazwa bazy danych
    'port': 3306,  # Port (domyślnie 3306 dla MySQL)
    #'ssl_ca': '/path/to/BaltimoreCyberTrustRoot.crt.pem'  # Ścieżka do certyfikatu SSL
}

app = Flask(__name__)

@app.route('/')
def index():
    conn = mysql.connector.connect(**config)
    # Tworzenie kursora
    cursor = conn.cursor()
    # Przykładowe zapytanie SQL
    query = "SELECT * FROM Clients"
    # Wykonanie zapytania
    cursor.execute(query)
    # Pobranie wyników
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')