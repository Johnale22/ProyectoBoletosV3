from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Ruta para crear un usuario
@app.route('/create', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data['name']
    email = data['email']
    
    connection = mysql.connector.connect(
        host='db',  # Nombre del contenedor de la base de datos
        user='root',
        password='rootpassword',
        database='testdb'
    )

    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    connection.commit()
    
    return jsonify({"message": "Usuario creado con éxito"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
