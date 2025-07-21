## ## Online airline ticket sales project

This project involves developing an online airline ticket sales system using microservices in AWS and automation with GitHub Actions.

---

## 📱 What does the system do?

1. A user registers or logs into the system.
2. Once logged in, they can purchase tickets, edit them, or delete them from their cart.
3. Upon purchase, a message is sent with the seat details, location, date, and flight details.
4. 

---

## GitHub repository link
https://github.com/Johnale22/ProyectoBoletosV3.git

---

## 🧱 Modular architecture

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

## 🧑‍💻 Author
- Universidad Central del Ecuador
- Facultad de Ingenieria y Ciencias Aplicadas
- Sistemas de Informacion
- Mineria de Datos
- John Guerra
- SIS8-001