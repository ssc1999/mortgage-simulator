# **Roams Mortgage Simulator API**

This project is a RESTful API that simulates mortgage calculations for clients. It is built using **FastAPI** and uses **SQLite** as the database. The API allows creating clients, retrieving their information, running mortgage simulations, and managing client data.

---

## **Features**
- **Create a Client**: Add a new client with their personal and financial details.
- **Retrieve Client Data**: Fetch client details by their DNI.
- **Simulate a Mortgage**: Calculate monthly payments and total repayment amount for a given TAE and amortization period.
- **Update/Delete Clients**: Modify or remove client information.
- **Input Validation**: Ensures data validity, including DNI and email format.
- **Interactive API Documentation**: Swagger UI available for testing endpoints.

---

## **Technologies**
- **Language**: Python
- **Framework**: FastAPI
- **Database**: SQLite
- **Validation**: Pydantic

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/roams-mortgage-simulator.git
cd roams-mortgage-simulator
```

### **2. Set Up the Environment**
Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate
.\venv\Scripts\activate   # Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### **3. Run the Server**
Start the FastAPI development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**  
Interactive documentation: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**  

---

## **Endpoints**

### **1. Create a Client**
- **POST** `/clients/`
- **Body**:
  ```json
  {
    "nombre": "Sergio Salgado",
    "dni": "12345678Z",
    "email": "sergio@gmail.com",
    "capital": 150000
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "nombre": "Sergio Salgado",
    "dni": "12345678Z",
    "email": "sergio@gmail.com",
    "capital": 150000
  }
  ```

### **2. Get Client by DNI**
- **GET** `/clients/{dni}`
- **Response**:
  ```json
  {
    "id": 1,
    "nombre": "Sergio Salgado",
    "dni": "12345678Z",
    "email": "sergio@gmail.com",
    "capital": 150000
  }
  ```

### **3. Simulate a Mortgage**
- **POST** `/mortgage/`
- **Body**:
  ```json
  {
    "dni": "12345678Z",
    "tae": 3.5,
    "plazo": 30
  }
  ```
- **Response**:
  ```json
  {
    "cuota_mensual": 673.58,
    "importe_total": 242489.52
  }
  ```

### **4. Update/Delete a Client**
- **PUT** `/clients/{dni}/`
- **DELETE** `/clients/{dni}/`

---

## **Testing the API**

### **Using Swagger UI**
Access the interactive API documentation at **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**. You can test all endpoints directly from your browser.

### **Using Postman**
1. Import the API endpoints into Postman.
2. Test each endpoint using the required input data.

### **Using `curl`**
Run commands like:
```bash
curl -X POST "http://127.0.0.1:8000/clients/" \
-H "Content-Type: application/json" \
-d '{"nombre": "Sergio Salgado", "dni": "12345678Z", "email": "sergio@gmail.com", "capital": 150000}'
```

---

## **Docker (Optional)**

### **Build the Docker Image**
```bash
docker build -t roams-mortgage-simulator .
```

### **Run the Docker Container**
```bash
docker run -p 8000:8000 roams-mortgage-simulator
```

The API will be available at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## **Project Structure**
```
roams-mortgage-simulator/
├── app/
│   ├── __init__.py
│   ├── main.py          # Entry point
│   ├── models.py        # Database models
│   ├── schemas.py       # Request/response schemas
│   ├── crud.py          # DB operations
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── clients.py   # Endpoints for clients
│   │   ├── mortgage.py  # Endpoints for mortgage simulations
│   └── utils.py         # Helper functions (e.g., DNI validation)
├── database.db          # SQLite database
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── Dockerfile           # Docker configuration
```

---