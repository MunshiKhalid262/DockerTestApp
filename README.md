# DockerTestApp

# 🐳 Dockerized Flask + React + MongoDB App

This is a fullstack application using **Flask (Python)** for the backend, **React** for the frontend, and **MongoDB** as the database — all containerized using **Docker** and managed via **Docker Compose**. CI/CD is handled through **GitHub Actions**.

---

## 📁 Project Structure

```
project-root/
├── backend/               # Flask backend
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/              # React frontend
│   ├── src/
│   ├── package.json
│   └── Dockerfile
│
├── docker-compose.yml    # Compose file to run fullstack
├── .github/workflows/    # GitHub Actions CI/CD
│   └── deploy.yml
└── README.md              # This file
```

---

## 🚀 Quick Start

Make sure you have **Docker** and **Docker Compose** installed.

### Run the App
```bash
docker-compose up --build
```

### Access the App
- Frontend: [http://localhost:3000](http://localhost:3000)
- Backend API: [http://localhost:5000](http://localhost:5000)
- MongoDB: accessible on `localhost:27017`

---

## ⚙️ Backend (Flask)

Located in the `backend/` folder.

### Features
- Flask app with CORS support
- Connects to MongoDB
- Sample `/` route returns document count

### Environment
`MONGO_URI` is configured via Docker Compose:
```yaml
environment:
  - MONGO_URI=mongodb://mongo:27017/DockerTest
```

---

## 🧩 Frontend (React)

Located in the `frontend/` folder.

### Features
- Fetches data from Flask API on load
- Display message returned by backend

### Development
To work outside Docker:
```bash
cd frontend
npm install
npm start
```

---

## 🔁 CI/CD Pipeline

CI/CD is configured using **GitHub Actions** in `.github/workflows/deploy.yml`.

### Trigger
- Pipeline runs **on push to `main` branch**

### Workflow Steps
- Checks out code
- Builds Docker containers
- Lists running containers
- Tears down after testing

---

## 📦 Build & Test Commands

### Build Only
```bash
docker-compose build
```

### Stop Containers
```bash
docker-compose down
```

### View Logs
```bash
docker-compose logs
```

---

## 🧼 Cleanup

Remove containers and images:
```bash
docker system prune -a --volumes
```

---

## ✅ Future Enhancements
- Add automated tests to CI workflow
- Deploy on AWS EC2 with SSH/CD integration
- Add support for environment variable configs

