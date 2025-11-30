# Task Analyzer

Task Analyzer is a simple full-stack application built to create and manage tasks.  
The main idea of the project is to let users enter a task, set how important it is, add a due date, and mention how many hours the task will take. The project uses Django for the backend API and React for the frontend UI.

## What the Project Does

- Lets the user add a task with:
  - Title
  - Importance level
  - Due date
  - Estimated hours
- Stores all tasks in a SQLite database
- Displays every task clearly on the frontend
- Connects the React UI to Django through an API
- Backend handles creating, updating, listing, and deleting tasks

The project is small and focused only on task handling. There are no extra features like login or filters unless they are added later.

## Project Structure

```
project-root/
│── db.sqlite3
│── manage.py
│── requirements/
│── tasks/               # App that contains models, views, serializers
│── task_analyzer/       # Django project configuration
│── frontend/            # React code for the UI
│── venv/                # Virtual environment (Windows)
└── README.md
```

## How to Run the Backend (Windows)

1. Activate the virtual environment:
```
venv\Scripts\activate
```

2. Install required packages:
```
pip install -r requirements.txt
```

3. Apply migrations:
```
python manage.py migrate
```

4. Start the backend server:
```
python manage.py runserver
```

Backend runs at:
http://127.0.0.1:8000/

## How to Run the Frontend

1. Go into the frontend folder:
```
cd frontend
```

2. Install dependencies:
```
npm install
```

3. Start the frontend:
```
npm start
```

Frontend runs at:
http://localhost:3000/

## API Overview

The backend exposes these endpoints:

- GET `/tasks/` – returns all tasks
- POST `/tasks/` – creates a new task
- GET `/tasks/<id>/` – returns one task
- PUT `/tasks/<id>/` – updates a task
- DELETE `/tasks/<id>/` – deletes a task

Each task contains:
- Title  
- Importance  
- Due date  
- Hours  

## Purpose of This Project

This project was built mainly to practice:
- Django REST Framework
- API development
- React frontend development
- Connecting frontend and backend
- Basic CRUD operations

It is kept simple on purpose, so it is easier to expand later with features like filtering, sorting, authentication, or dashboards.

