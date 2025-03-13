from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

config = {
    'user': 'wbsadmin',  # Nazwa użytkownika bazy danych
    'password': 'Testowe7',  # Hasło użytkownika
    'host': 'wbspython2025.mysql.database.azure.com',  # Nazwa serwera Azure MySQL
    'database': 'wbspython2025',  # Nazwa bazy danych
    'port': 3306,  # Port (domyślnie 3306 dla MySQL)
    # 'ssl_ca': '/path/to/BaltimoreCyberTrustRoot.crt.pem'  # Ścieżka do certyfikatu SSL
}

app = Flask(__name__)


@app.route('/')
def index():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    query = "SELECT * FROM Clients"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', data=data)


@app.route('/add', methods=['POST'])
def add_client():
    name = request.form['name']
    city = request.form['city']
    sales = request.form['sales']

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    query = "INSERT INTO Clients (Name, City, Sales) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, city, sales))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')