from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'Raghav' #default value
    age: Optional[int] = None
    cgpa: float = Field(gt=0, lt =10, default = 5)

new_student = {'age':22 , 'email': 'raghavag122@gmail.com'}

student = Student(**new_student)

print(student)
