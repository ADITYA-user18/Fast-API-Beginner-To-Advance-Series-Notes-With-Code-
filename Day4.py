# Import necessary things
from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional, List, Dict, Annotated


# -----------------------------
# 1️⃣ Basic Model with Required Fields
# -----------------------------

class Developer(BaseModel):
    # Required string field
    name: str
    
    # Required integer field
    age: int
    
    # Required message
    msg: str


# Creating object (validation happens here)
dev1 = Developer(name="Aditya", age=22, msg="Learning FastAPI")
print(dev1)
print(dev1.age)  # Access like object.attribute


# -----------------------------
# 2️⃣ Using Field() for Metadata and Constraints
# -----------------------------

class Employee(BaseModel):
    # ... means REQUIRED field
    name: str = Field(..., description="Employee full name")
    
    # Age must be > 18 and < 60
    age: int = Field(..., gt=18, lt=60)
    
    # Minimum 5 characters required
    department: str = Field(..., min_length=5)


emp = Employee(name="John Doe", age=30, department="Sales")
print(emp)


# -----------------------------
# 3️⃣ Default Values
# -----------------------------

class Student(BaseModel):
    name: str
    grade: str = "A"  # Default value


stu = Student(name="Rahul")
print(stu.grade)  # Output: A


# -----------------------------
# 4️⃣ Optional Fields
# -----------------------------

class User(BaseModel):
    username: str
    bio: Optional[str] = None  # Optional field


user1 = User(username="adi")
print(user1.bio)  # None


# -----------------------------
# 5️⃣ Annotated (Advanced Type Hinting)
# -----------------------------

# Annotated lets us combine type + constraints
class Product(BaseModel):
    price: Annotated[float, Field(gt=0)]
    quantity: Annotated[int, Field(ge=1)]


product = Product(price=10.5, quantity=3)
print(product)


# -----------------------------
# 6️⃣ Useful Built-in Types
# -----------------------------

class Account(BaseModel):
    email: EmailStr  # Validates email format
    tags: List[str]  # List of strings
    metadata: Dict[str, str]  # Dictionary


account = Account(
    email="test@gmail.com",
    tags=["admin", "premium"],
    metadata={"country": "India"}
)

print(account)


# -----------------------------
# 7️⃣ Automatic Type Conversion
# -----------------------------

class Order(BaseModel):
    item_id: int
    price: float


# Even if passed as string, Pydantic converts
order = Order(item_id="10", price="99.5")

print(order.item_id)  # 10 (int)
print(type(order.item_id))  # <class 'int'>


# -----------------------------
# 8️⃣ Nested Models
# -----------------------------

class Address(BaseModel):
    city: str
    pincode: int


class Customer(BaseModel):
    name: str
    address: Address  # Nested model


cust = Customer(
    name="Aditya",
    address={"city": "Mysore", "pincode": 570001}
)

print(cust.address.city)


# -----------------------------
# 9️⃣ Custom Validator
# -----------------------------

class Register(BaseModel):
    password: str

    @field_validator("password")
    def validate_password(cls, value):
        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters")
        return value


reg = Register(password="secure123")
print(reg)


# -----------------------------
# 🔟 Model Utility Methods
# -----------------------------

print(dev1.model_dump())  # Convert to dictionary
print(dev1.model_dump_json())  # Convert to JSON string