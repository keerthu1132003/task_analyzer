# Task Analyzer

Task Analyzer is a simple full-stack project that allows users to create and manage tasks.  
It is built with Django on the backend and React on the frontend.  
The project focuses only on task handling: adding tasks, setting importance, due dates, and hours.

---

## What the Project Does

- Lets the user create a task with:
  - Title
  - Importance value
  - Due date
  - Hours needed
- Shows all tasks on the frontend
- Stores data in a SQLite database
- Uses a Django REST API for all operations
- Supports basic CRUD (Create, Read, Update, Delete)

---

## How the Logic Is Written

This section explains how the backend and frontend work internally.

### 1. Backend Logic (Django REST Framework)

**Model (tasks/models.py)**  
Defines the structure of a task:

```python
class Task(models.Model):
    title = models.CharField(max_length=200)
    importance = models.IntegerField()
    due_date = models.DateField()
    hours = models.FloatField()
```

**Serializer (tasks/serializers.py)**  
Converts task objects to JSON and back:

```python
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
```

**Views (tasks/views.py)**  
Handles listing, creating, updating, and deleting tasks:

```python
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
```

**URLs (task_analyzer/urls.py)**  
Exposes the API:

```python
urlpatterns = [
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
]
```

---

### 2. Frontend Logic (React)

**Fetching tasks**

```javascript
useEffect(() => {
  axios.get("http://127.0.0.1:8000/tasks/")
    .then(res => setTasks(res.data));
}, []);
```

**Adding a task**

```javascript
axios.post("http://127.0.0.1:8000/tasks/", {
  title,
  importance,
  due_date,
  hours
});
```

**Updating a task**

```javascript
axios.put(`http://127.0.0.1:8000/tasks/${id}/`, updatedData);
```

**Deleting a task**

```javascript
axios.delete(`http://127.0.0.1:8000/tasks/${id}/`);
```

---

### 3. Full System Flow

1. React sends data to Django  
2. Django saves tasks in the database  
3. React fetches tasks and displays them  
4. Any update or delete goes through the API  
5. UI updates after every operation  

---

## Project Structure

```
project-root/
│── db.sqlite3
│── manage.py
│── requirements/
│── tasks/
│── task_analyzer/
│── frontend/
│── venv/
└── README.md
```

---

## Backend Setup (Windows)

1. Activate virtual environment:
```
venv\Scripts\activate
```

2. Install requirements:
```
pip install -r requirements.txt
```

3. Apply migrations:
```
python manage.py migrate
```

4. Run the server:
```
python manage.py runserver
```

Backend URL:
http://127.0.0.1:8000/

---

## Frontend Setup

1. Go to frontend:
```
cd frontend
```

2. Install packages:
```
npm install
```

3. Start the app:
```
npm start
```

Frontend URL:
http://localhost:3000/

---

## API Endpoints

- GET /tasks/  
- POST /tasks/  
- GET /tasks/<id>/  
- PUT /tasks/<id>/  
- DELETE /tasks/<id>/  

---



