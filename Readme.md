# Flask + MySQL Signup API

This project is a simple Flask API connected to a MySQL database using Docker.  
It includes:
- A `/api/signup` endpoint for creating users
- MySQL database setup with an initialization script (`db.sql`)
- Docker Compose configuration for easy deployment

---

## **Project Structure**

src/
app.py                # Flask application
database/
db.sql              # SQL script to create tables
docker-compose.yml      # Docker setup for MySQL
requirements.txt        # Python dependencies

---

## **Prerequisites**
- [Python 3.11+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## **Setup**

### 1. Clone the Repository
```bash
git clonehttps://github.com/Emmanuelonyo/MIVA-CSC312.git
cd MIVA-CSC312

2. Start MySQL with Docker

docker compose up -d

This will start MySQL, create CSC312_db, and run the src/database/db.sql script.

⸻

3. Install Dependencies

pip install -r requirements.txt


⸻

4. Run Flask Locally

export FLASK_APP=src/app.py
flask run --port=8081

The API will be available at:

http://127.0.0.1:8081


⸻

5. Test the API

Create a New User

curl -X POST http://127.0.0.1:8081/api/signup \
-H "Content-Type: application/json" \
-d '{"username": "john_doe", "password": "securepass"}'


⸻

Database
	•	Name: CSC312_db
	•	User: root (if running locally) mysql (if using docker)
	•	Password: root
	•	Table: tbl_user

The users table includes:
	•	id (auto-increment primary key)
	•	username (unique)
	•	password (hashed recommended)
	•	created_at
	•	updated_at

⸻

Notes
	•	This setup is for development only.
	•	For production, use a production WSGI server like gunicorn and secure environment variables.

---