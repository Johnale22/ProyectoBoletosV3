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
├── Microservices/         
   ├── Databases/            
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
        ├── airline_integration/                  
   ├── Infraestructure/                      
       ├── ApiGateway/ 
   ├── Reports/
   ├── Reservations/
   ├── Users/
       ├── audit_logs/
       ├── authentication/
       ├── authorization/
       ├── password_recovery/
       ├── user_management/        
   └── Notifications/                                  
```

## 🧑‍💻 Autor
- Universidad Central del Ecuador
- Facultad de Ingenieria y Ciencias Aplicadas
- Sistemas de Informacion
- Mineria de Datos
- John Guerra
- SIS8-001