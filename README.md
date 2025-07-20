## ## Proyecto venta de boletos de avion en linea

Este proyecto consiste en el desarrollo de un sistema de **venta de boletos de avion en linea** usando  y una aplicacion movil, usando microservicios en aws y automatizacion con github actions.

---

## 📱 ¿Qué hace el sistema?

1. Un usuario se registra o loguea en el sistema
2. Una vez dentro puede comprar pasajes, editarlos u eliminarlos del carrito
3. Con la compra se le envia un mensaje diciendo los datos del asiento, ubicacion, fecha y avíon
4. 

---

## Link de repositorio GitHub
https://github.com/Johnale22/ProyectoBoletosV3.git

---

## 🧱 Arquitectura por módulos

```bash
ProyectoBoletosV3/
├── Microservices/         # Microservicio ordenados por dominios
   ├── Databases/            # Microservicio de inferencia (Gemini)
       ├── Cassandra/
       ├── Minio/ 
       ├── Mongo/ 
       ├── Mysql/ 
       ├── Postgrest/
       ├── Redis/   
   ├── Flights/
        ├── flight_catalog/
        ├── flight_availability/
        ├── pricing_engine/
        ├── inventory_management/
        ├── airline_integration/                  # Microservicio unificado (YOLO + Gemini)
   ├── Infraestructure/                      # Orquestador de los 3 servicios
       ├── ApiGateway/ 
   ├── Reports/
   ├── Reservations/
   ├── Users/
       ├── audit_logs/
       ├── authentication/
       ├── authorization/
       ├── password_recovery/
       ├── user_management/        
   └── Notifications/                                   # Documentación adicional
```

## ⚙️ Tecnologías utilizadas

| Componente           | Tecnología                   |
| -------------------- | ---------------------------- |
| Backend REST         | Python + FastAPI             |
| Visión computacional | YOLOv8 (`ultralytics`)       |
| IA generativa        | Gemini 2.0 Flash (Google AI) |
| Contenedores         | Docker                       |
| Orquestación         | Docker Compose               |
| Comunicación         | API REST (JSON + Imágenes)   |

---

## 🚀 Cómo levantar Docker Compose

Asegurarse de tener un archivo .env en Modulo_2_Gemini_Vehicle_Info/ con tu API Key ya que en GitHub no se sube el archivo:

```bash
GEMINI_API_KEY=api_key
```
Luego, desde la raíz del proyecto (PROYECTO_FINAL/):

```bash
docker compose up --build
```

Esto levantará automáticamente:
- yolo-detector en http://localhost:8000
- gemini-analyzer en http://localhost:8001
- unified-api en http://localhost:8002

---

## 📦 Flujo de trabajo actual

🔁 Flujo completo con microservicio unificado
1. El usuario sube una imagen a POST /analyze
2. El sistema:
   * Detecta el vehículo con YOLO
   * Recorta automáticamente
   * Analiza la imagen con Gemini
3. Devuelve toda la información del vehículo en formato JSON:

Prueba el endpoint en:
📍 http://localhost:8002/docs

---

## 🧪 Pruebas individuales
También puedes acceder a los microservicios por separado:
   * YOLO → POST /detect en http://localhost:8000
   * Gemini → POST /analyze en http://localhost:8001

---

## 🧑‍💻 Autores
- Universidad Central del Ecuador
- Facultad de Ingenieria y Ciencias Aplicadas
- Sistemas de Informacion
- Mineria de Datos
- Yoshua Calahorrano y John Guerra
- SIS8-001