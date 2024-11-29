# Flask API Drinks Demo

A simple Flask-based API for managing drinks. This project demonstrates the use of Flask and Flask-SQLAlchemy for building RESTful APIs.

---

## **API**

### **Learning about API**
- **Date**: 29 Nov 2024
- **Reference Video**: [Learn Flask API - YouTube](https://www.youtube.com/watch?v=qbLc5a9jdXo)

### **What is an API?**
- **API** (Application Program Interface) helps two software systems communicate with each other.
- Returns data in **JSON** (JavaScript Object Notation) format.
- Enhances application security by exposing only the required data to the client (e.g., using IDs or tags).

### **Methods in REST API**
- **GET**: Retrieve Data (Read)
- **POST**: Write data to the server (Create)
- **DELETE**: Delete data from the server (Delete)
- **PUT**: Update Data (Update)

> **CRUD operations in database terms:**
> - Create, Read, Update, Delete.

### **Key Notes**
- **POST**: Adding duplicate data causes errors. Example: Adding "cola" twice with `POST` will result in a conflict.
- **PUT**: Allows updating the data repeatedly without causing issues.

---

## **How to Run the Project**

### **Requirements**
1. **Python**: Version 3.6 or higher.
2. **Flask**: Install using `pip install flask`.
3. **Flask-SQLAlchemy**: Install using `pip install flask_sqlalchemy`.

### **Steps to Run**
```bash
git clone https://github.com/<your-username>/flask-api-drinks-demo.git
cd flask-api-drinks-demo

from app import db
db.create_all()
python app.py
# Open the browser or use Postman to test endpoints.

