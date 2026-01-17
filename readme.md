# Employee Management REST API

## Overview

This project is a **Django REST Framework–based Employee Management API** built as part of the **HabotConnect Python Backend Hiring Assignment**.

The API allows authenticated users to **create, read, update, and delete employee records**, following **RESTful principles**, correct **HTTP status codes**, **JWT-based authentication**, **pagination**, **filtering**, and **unit testing best practices**.

---

## Features

* JWT-based authentication
* CRUD operations for employees
* Input validation and proper error handling
* Pagination (10 records per page)
* Filtering by department and role
* Secure endpoints (authenticated access only)
* Unit tests covering major flows and edge cases
* Clean, modular project structure

---

## Tech Stack

* Python 3.x
* Django
* Django REST Framework
* Simple JWT (Authentication)
* SQLite (default database)
* Postman (for API testing and demo)

---

## Project Setup Instructions

### 1. Clone the Repository

git clone <your-repo-url>
cd employee_mgmt

---

### 2. Create & Activate Virtual Environment

python -m venv venv

Windows

venv\Scripts\activate

Mac / Linux

source venv/bin/activate

---

### 3. Install Dependencies

pip install -r requirements.txt

pip freeze > requirements.txt

---

### 4. Run Database Migrations

python manage.py makemigrations
python manage.py migrate

---

### 5. Create Superuser

python manage.py createsuperuser

This user will be used for authentication and testing.

---

### 6. Start Development Server

python manage.py runserver

Server will be available at:
http://127.0.0.1:8000/

---

## Authentication (JWT)

### Obtain Access Token

Endpoint

POST /api/token/

Request Body

json
{
  "username": "your_username",
  "password": "your_password"
}

Response

{
  "access": "<jwt_access_token>",
  "refresh": "<jwt_refresh_token>"
}

---

### Using Token in Requests

In Postman:

* Go to **Authorization**
* Type: `Bearer Token`
* Paste the **access token**

All employee APIs require authentication.

---

## API Endpoints

### Create Employee

**POST** `/api/employees/`

json
{
  "name": "Anuj Dwivedi",
  "email": "anuj@example.com",
  "department": "Engineering",
  "role": "Developer"
}

**Success**

* `201 Created`

**Errors**

* `400 Bad Request` (duplicate email, empty name)

---

### List Employees

**GET** `/api/employees/`

**Pagination**

/api/employees/?page=2

**Filtering**

/api/employees/?department=HR
/api/employees/?role=Developer

**Success**

* `200 OK`

---

### Retrieve Employee

**GET** `/api/employees/{id}/`

**Success**

* `200 OK`

**Error**

* `404 Not Found`

---

### Update Employee

**PUT** `/api/employees/{id}/`

json
{
  "name": "Updated Name",
  "email": "anuj@example.com",
  "department": "HR",
  "role": "Manager"
}

**Success**

* `200 OK`

---

### Delete Employee

**DELETE** `/api/employees/{id}/`

**Success**

* `204 No Content`

---

## Testing

Run all unit tests using:

python manage.py test


### Test Coverage Includes:

* JWT authentication
* Employee creation
* Duplicate email validation
* Employee retrieval (valid & invalid ID)
* Update operations
* Delete operations
* Pagination behavior


## Design Decisions & Best Practices

* Used **Django REST Framework Generic Views** to reduce boilerplate and improve clarity
* Enforced **database-level constraints** for data integrity
* Implemented **JWT authentication** for stateless and secure access
* Added **global pagination** for consistent API behavior
* Handled edge cases with proper HTTP status codes
* Wrote unit tests to validate business logic and API stability

---

## Presentation Flow (Interview Demo)

1. Obtain JWT token
2. Add token to Postman authorization header
3. Create an employee
4. Show duplicate email validation error
5. List employees with pagination
6. Filter employees by department or role
7. Retrieve employee by ID (success + 404 case)
8. Update employee details
9. Delete employee and verify `204 No Content`

---

## Conclusion

This project demonstrates a **clean, secure, and REST-compliant backend API**, following industry best practices and meeting all requirements specified in the HabotConnect hiring assignment.


{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2ODcyMzY4MSwiaWF0IjoxNzY4NjM3MjgxLCJqdGkiOiJiODExYWYzOGI0Njc0MjkyYmQ5ZDYzMzFkZDFmYWZlMyIsInVzZXJfaWQiOiIxIn0.kLebof7Xvs8PDarvTnpr4h_fSC6JO2NUrf1sRkba9ak",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY4NjQwODgxLCJpYXQiOjE3Njg2MzcyODEsImp0aSI6IjIzNDNiNmI4MWFhYzQ3MGM5MmE2MmJhYTIzMWQyMTQ5IiwidXNlcl9pZCI6IjEifQ.0I1Mdo-BIS89bCb9OlOMMos_c_PLWqbdRgc14ZqFlhg"
}