# Soccer Player Comparison App

This repository contains a minimal example of a web application for comparing soccer players. It uses a Python backend (FastAPI) and a React frontend. Player data is stored in a local SQLite database.

**Important:** Always check the terms of service of any third‑party website before scraping or using their data. The sample application uses placeholder data loaded by `seed_data.py`. Replace this with data from a source you have permission to use (for example, an official API or a dataset you are licensed to access).

## Backend

1. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r backend/requirements.txt
   ```
2. Seed the database with sample data:
   ```bash
   python backend/app/seed_data.py
   ```
3. Run the server:
   ```bash
   uvicorn backend.app.main:app --reload
   ```
   The API will be available at `http://localhost:8000`.

## Frontend

This is a minimal React setup. Install dependencies (requires Node.js) and start the development server:

```bash
cd frontend
npm install
npm start
```

The app will connect to the backend at `http://localhost:8000`.

## Deploying

You can host the backend and frontend on an EC2 instance. A simple approach is to run the FastAPI app with a production server such as `uvicorn` or `gunicorn`, and serve the React build using `serve` or from a web server like Nginx. If you prefer infrastructure as code, tools like Terraform or AWS CloudFormation can automate provisioning the EC2 instance.
