# To Understand the Pydantics  dto model and validation features, we will create a simple Bank Customer model. This model will include fields like name, age, email, phone number, and account type. We will also implement a custom validator to ensure that the email provided belongs to an HDFC Bank user.

from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Annotated, Optional


# -----------------------------
# 🏦 Bank Customer Model
# -----------------------------

class BankCustomer(BaseModel):
    
    # Full name (minimum 3 characters)
    name: Annotated[str, Field(min_length=3, description="Customer full name")]
    
    # Age must be between 18 and 100
    age: Annotated[int, Field(gt=17, lt=101)]
    
    # Email validation (must be proper email format)
    email: EmailStr
    
    # Optional phone number
    phone: Optional[str] = None
    
    # Account type with default value
    account_type: str = "Savings"
    
    
    # -----------------------------
    # 🔥 Custom Validator
    # -----------------------------
    
    @field_validator("email")
    def check_hdfc_email(cls, value):
        """
        Custom validation:
        Check whether email contains 'hdfc'
        """
        if "hdfc" not in value.lower():
            raise ValueError("Not a valid HDFC Bank user email")
        return value


# -----------------------------
# 🧪 Testing the Model
# -----------------------------

# ✅ Valid HDFC User
valid_user = {
    "name": "Aditya",
    "age": 22,
    "email": "aditya@hdfcbank.com"
}

customer1 = BankCustomer(**valid_user)
print("Verified HDFC User:", customer1)


# ❌ Invalid User
invalid_user = {
    "name": "Rahul",
    "age": 25,
    "email": "rahul@ghdfcmail.com"
}

try:
    customer2 = BankCustomer(**invalid_user)
except Exception as e:
    print("Verification Failed:", e)