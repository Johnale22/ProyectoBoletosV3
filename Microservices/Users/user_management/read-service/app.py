from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Ruta para leer usuarios
@app.route('/read', methods=['GET'])
def get_users():
    connection = mysql.connector.connect(
        host='54.85.19.110',
        user='user',
        password='12345',
        database='mysqldb'
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    users_list = [{"id": user[0], "name": user[1], "email": user[2]} for user in users]
    
    return jsonify(users_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
