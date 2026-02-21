from pydantic import BaseModel, Field


class Devel0per(BaseModel):
    name: str = Field(..., description="The name of the developer")
    age: int = Field(..., description="The age of the developer")
    msg: str = Field(..., description="A message from the developer")


raw_data = {
    'name': 'John Doe',
    'age': 30,
    'msg': 'This is the Patients Management System'
}

ready_data = Devel0per(**raw_data)


def about(dev: Devel0per):
    print(f"Developer Name: {dev.name}")
    print(f"Age: {dev.age}")
    print(f"Message: {dev.msg}")


about(ready_data)