from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

import uvicorn

app = FastAPI()



class CreateEditCourse(BaseModel):
    name: str
    short_description: str
    price: float

class Course(BaseModel):
    id: int
    name: str
    short_description: str
    price: float

courses = [
	{
		'id': 1,
		'name': 'Business Fundamentals',
		'short_description': 'This course will get you acquainted with busines',
		'price': 20.0
	},
	{
		'id': 2,
		'name': 'Math Fundamentals',
		'short_description': 'This course will get you acquainted with math',
		'price': 50.0
	},
	{
		'id': 3,
		'name': 'Programming Fundamentals',
		'short_description': 'This course will get you acquainted with programming',
		'price': 100500.0
	}
]

my_courses: List[Course] = courses

@app.get("/")
def get_root():
    return {"<h1>Welcome to Oleksii's Fast API example"}


@app.get("/api/v1.0/courses", response_model=List[Course])
def get_courses():
    return my_courses

@app.get("/api/v1.0/courses/{course_id}", response_model=Course)
def get_course(course_id: int):
    course = next(filter(lambda course: course['id'] == course_id, courses), False)
    return course

@app.post("/api/v1.0/courses", response_model=Course, status_code=201)
def create_course(course: CreateEditCourse):
    course = {
        'id': courses[-1]['id'] + 1,
        'name': course.name,
        'short_description': course.short_description,
        'price': course.price
    }
    courses.append(course)
    return course

@app.put("/api/v1.0/courses/{course_id}", response_model=Course)
def edit_course(course_id: int, course: CreateEditCourse):
    newCourse = {
        'id': course_id,
        'name': course.name,
        'short_description': course.short_description,
        'price': course.price
    }
    return newCourse

@app.delete("/api/v1.0/courses/{course_id}", response_model=List[Course], status_code=201)
def delete_course(course_id: int):
    course = list(filter(lambda t: t['id'] != course_id, courses))
    return course
