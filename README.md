# assignment-13-student-api

Student API with validated GET, POST, PUT and DELETE routes.

## Run

Requires Python 3.10+. From this repository folder:

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs in your browser. 

## Routes

- GET /students and GET /students/{student_id}
- POST /students: `{"name":"Chetan","course":"Python","email":"chetan@example.com"}` (email optional)
- PUT /students/{student_id}: same fields
- DELETE /students/{student_id}

Interactive documentation: http://127.0.0.1:8000/docs

POST returns 201; DELETE returns 204; missing records return 404; invalid input returns 422. IDs come from the server. Records are stored in server memory: browser refresh retains records while the server is running, but restarting the server resets them. Run with one worker for this assignment.

## Tests

```powershell
.venv\Scripts\python -m pip install pytest httpx
.venv\Scripts\python -m pytest -q
```
