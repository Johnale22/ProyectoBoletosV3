from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data['name']
    email = data['email']

    connection = mysql.connector.connect(
        host='54.85.19.110',
        user='user',
        password='12345',
        database='mysqldb'
    )

    cursor = connection.cursor()
    cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
    connection.commit()

    return jsonify({"message": "Usuario actualizado con éxito"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
