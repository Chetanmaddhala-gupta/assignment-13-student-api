from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, ConfigDict, Field

app = FastAPI(title="Student API", description="Student records with validated CRUD routes", version="2.0.0")

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

class StudentInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    name: str = Field(min_length=1)
    course: str = Field(min_length=1)
    email: str = ""


class Student(StudentInput):
    id: int


next_student_id = 4


@app.post("/students", response_model=Student, status_code=201, tags=["Students"])
def create_student(student: StudentInput):
    global next_student_id
    record = {"id": next_student_id, **student.model_dump()}
    next_student_id += 1
    students.append(record)
    return record


@app.put("/students/{student_id}", response_model=Student, tags=["Students"])
def update_student(student_id: int, student: StudentInput):
    record = get_student(student_id)
    record.update(student.model_dump())
    return record


@app.delete("/students/{student_id}", status_code=204, tags=["Students"])
def delete_student(student_id: int):
    students.remove(get_student(student_id))
    return Response(status_code=204)
