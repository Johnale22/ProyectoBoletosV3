# Usa una imagen base de Python
FROM python:3.9-slim

# Crea un directorio para la aplicación
WORKDIR /app

# Copia los archivos de la aplicación
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

# Expone el puerto 5000
EXPOSE 5002

# Comando para iniciar la aplicación
CMD ["python", "app.py"]
