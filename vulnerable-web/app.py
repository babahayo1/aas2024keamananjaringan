from flask import Flask, request, render_template_string
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Vulnerable Web Application!"

@app.route('/sql_injection')
def sql_injection():
    user_id = request.args.get('id')
    connection = mysql.connector.connect(
        host='db',
        user='user',
        password='password',
        database='mydb'
    )
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    result = cursor.fetchall()
    connection.close()
    return str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
