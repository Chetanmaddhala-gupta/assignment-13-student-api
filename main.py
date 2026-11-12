from fastapi import FastAPI, HTTPException

app = FastAPI(title="Student API", description="A beginner API with GET routes", version="1.0.0")

students = [
    {"id": 1, "name": "Asha Rao", "course": "Python"},
    {"id": 2, "name": "Rahul Das", "course": "Web Development"},
    {"id": 3, "name": "Meera Shah", "course": "FastAPI"},
]


@app.get("/", tags=["Home"])
def home():
    return {"message": "Welcome to the Student API", "docs": "/docs"}


@app.get("/students", tags=["Students"])
def get_students():
    return students


@app.get("/students/{student_id}", tags=["Students"])
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")
