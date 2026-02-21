"""
ADVANCED PYDANTIC COMPLETE EXAMPLE
Covers:
- Field validation
- Model validation
- Computed fields
- Nested models
- Serialization
"""

from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    field_validator,
    model_validator,
    computed_field
)
from typing import List, Optional
from datetime import datetime


# ======================================================
# 1️⃣ Nested Model: Address
# ======================================================

class Address(BaseModel):
    """
    Nested model representing customer's address.
    This will be used inside Customer model.
    """
    city: str
    pincode: int


# ======================================================
# 2️⃣ Main Model: Customer
# ======================================================

class Customer(BaseModel):
    """
    Main customer model.
    Demonstrates:
    - Field validation
    - Model validation
    - Computed fields
    - Nested models
    """

    # Basic Fields
    name: str = Field(..., min_length=3)
    age: int = Field(..., gt=17)
    email: EmailStr

    # Optional field
    phone: Optional[str] = None

    # Nested model
    address: Address

    # List type
    account_types: List[str]

    # Date field
    created_at: datetime


    # ==================================================
    # 3️⃣ Field Validator (Validates Single Field)
    # ==================================================

    @field_validator("email")
    def check_hdfc_email(cls, value):
        """
        Custom field validation:
        Email must contain 'hdfc'
        """
        if "hdfc" not in value.lower():
            raise ValueError("Email must belong to HDFC bank")
        return value


    # ==================================================
    # 4️⃣ Model Validator (Validates Whole Model)
    # ==================================================

    @model_validator(mode="after")
    def check_account_rules(self):
        """
        Model-level validation:
        If customer has 'Loan' account,
        age must be greater than 21
        """
        if "Loan" in self.account_types and self.age <= 21:
            raise ValueError("Loan account requires age > 21")
        return self


    # ==================================================
    # 5️⃣ Computed Field (Calculated Automatically)
    # ==================================================

    @computed_field
    @property
    def is_adult(self) -> bool:
        """
        Computed field:
        Automatically calculates if customer is adult.
        """
        return self.age >= 18


    @computed_field
    @property
    def account_summary(self) -> str:
        """
        Computed summary string
        """
        return f"{self.name} has {len(self.account_types)} accounts."


# ======================================================
# 6️⃣ Testing the Model
# ======================================================

if __name__ == "__main__":

    # Raw input data (like API request data)
    raw_data = {
        "name": "Aditya",
        "age": 25,
        "email": "aditya@hdfcbank.com",
        "phone": "9876543210",
        "address": {
            "city": "Mysore",
            "pincode": 570001
        },
        "account_types": ["Savings", "Loan"],
        "created_at": "2026-02-21T15:00:00"
    }

    # Create Pydantic object (validation happens here)
    customer = Customer(**raw_data)

    print("\n✅ Customer Object:")
    print(customer)

    # ==================================================
    # 7️⃣ Accessing Computed Fields
    # ==================================================
    print("\n🔹 Computed Fields:")
    print("Is Adult:", customer.is_adult)
    print("Account Summary:", customer.account_summary)

    # ==================================================
    # 8️⃣ Serialization
    # ==================================================

    print("\n🔹 Serialized to Dictionary:")
    print(customer.model_dump())   # Convert model to dict

    print("\n🔹 Serialized to JSON:")
    print(customer.model_dump_json(indent=2))  # Convert to JSON string