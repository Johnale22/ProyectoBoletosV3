from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Ruta para eliminar un usuario
@app.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    connection = mysql.connector.connect(
        host='db',
        user='root',
        password='rootpassword',
        database='testdb'
    )

    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    connection.commit()

    return jsonify({"message": "Usuario eliminado con éxito"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
