# Usamos la imagen oficial de Node.js
FROM node:14

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos del proyecto al contenedor
COPY . .

# Instalamos las dependencias
RUN npm install

# Exponemos el puerto 3001 para poder acceder al servicio
EXPOSE 3001

# Comando para iniciar la aplicación
CMD ["npm", "start"]
