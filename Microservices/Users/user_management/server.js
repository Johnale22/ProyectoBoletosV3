const express = require('express');
const mysql = require('mysql2');
const app = express();
const port = 3001;

// Configura la conexión a la base de datos MySQL
const db = mysql.createConnection({
  host: 'MySQLMS',  // El nombre del servicio en docker-compose
  user: 'user',  // El usuario de la base de datos
  password: '12345',  // La contraseña configurada
  database: 'mysqldb'  // El nombre de la base de datos
});

// Conectar a la base de datos
db.connect((err) => {
  if (err) {
    console.error('Error al conectar a la base de datos:', err.stack);
    return;
  }
  console.log('Conectado a la base de datos MySQL');
});

// Middleware para parsear JSON
app.use(express.json());

// Ruta para registrar un nuevo usuario
app.post('/users', (req, res) => {
  const { name, email } = req.body;
  
  if (!name || !email) {
    return res.status(400).send('Faltan datos');
  }

  // Inserta un nuevo usuario en la base de datos
  const query = 'INSERT INTO users (name, email) VALUES (?, ?)';
  db.query(query, [name, email], (err, result) => {
    if (err) {
      return res.status(500).send('Error al crear el usuario');
    }
    res.status(201).send(`Usuario creado con ID: ${result.insertId}`);
  });
});

// Ruta para obtener todos los usuarios
app.get('/users', (req, res) => {
  db.query('SELECT * FROM users', (err, results) => {
    if (err) {
      return res.status(500).send('Error al obtener los usuarios');
    }
    res.status(200).json(results);
  });
});

// Inicia el servidor
app.listen(port, () => {
  console.log(`Microservicio User Management corriendo en http://localhost:${port}`);
});
