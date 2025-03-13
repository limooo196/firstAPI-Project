from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
from datetime import datetime
import re

class User(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="Full name of the user")
    email: EmailStr = Field(..., description="Valid email address of the user")
    phone: Optional[str] = Field(
        None,
        pattern=r"^\+?[1-9]\d{9,14}$",  # Validate international phone numbers
        description="Optional phone number in international format (e.g., +6281234567890)"
    )
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Timestamp when the user was created")
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Timestamp when the user was last updated")

    @validator("name")
    def validate_name(cls, value):
        value = value.strip()
        if not re.match(r"^[a-zA-Z\s]+$", value):
            raise ValueError("Name must contain only letters and spaces")
        return value

    @validator("email")
    def validate_email(cls, value):
        # Remove leading/trailing spaces
        value = value.strip()
        # Basic email validation check (this can be improved if necessary)
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value):
            raise ValueError("Invalid email format")
        return value

    @validator("phone")
    def validate_phone(cls, value):
        if value is not None:
            # Check if the phone number matches the international format
            if not re.match(r"^\+?[1-9]\d{9,14}$", value):
                raise ValueError("Phone number must be in international format (e.g., +6281234567890)")
            # Optional: You could enforce a minimum length constraint here if needed
            if len(value) < 10:
                raise ValueError("Phone number must have at least 10 digits")
        return value

    # Ensure that 'updated_at' is updated automatically on any update
    def update_timestamp(self):
        self.updated_at = datetime.utcnow()

    def __str__(self):
        return f"User(name={self.name}, email={self.email}, phone={self.phone}, created_at={self.created_at}, updated_at={self.updated_at})"
