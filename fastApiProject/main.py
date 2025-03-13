from firebase import db
from fastapi import FastAPI, HTTPException
from firebase_admin import firestore, initialize_app
from models import BaseModel,User
from datetime import datetime
from fastapi.encoders import jsonable_encoder


# Initialize Firebase app (make sure Firebase is properly configured)

app = FastAPI()

# Firestore reference
db = firestore.client()


# Create User
@app.post("/users/", response_model=User)
async def create_user(user: User):
    try:
        user_dict = user.dict()  # This will trigger Pydantic validation
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

    # Check if user already exists
    user_ref = db.collection("users").document(user.email)
    if user_ref.get().exists:
        raise HTTPException(status_code=400, detail="User already exists")

    # Add created_at timestamp
    user_dict['created_at'] = user.created_at
    user_dict['updated_at'] = user.updated_at

    # Create user in Firestore
    user_ref.set(user_dict)
    return user

# Read User
@app.get("/users/{email}", response_model=User)
async def get_user(email: str):
    user_ref = db.collection("users").document(email)
    user_doc = user_ref.get()
    if not user_doc.exists:
        raise HTTPException(status_code=404, detail="User not found")
    return user_doc.to_dict()

# Read ALL Users

@app.get("/users/", response_model=list[User])
async def get_all_users():
    users_ref = db.collection("users")
    users = users_ref.stream()  # Get all documents in the 'users' collection

    # Fetch all user data and convert to a list
    all_users = []
    for user_doc in users:
        user_data = user_doc.to_dict()  # Get the user data as a dictionary
        all_users.append(user_data)  # Add the user data to the list

    # Return all users
    return jsonable_encoder(all_users)  # Ensure proper encoding for the response

# Update User
@app.put("/users/{email}", response_model=User)
async def update_user(email: str, user: User):
    user_ref = db.collection("users").document(email)
    user_doc = user_ref.get()
    if not user_doc.exists:
        raise HTTPException(status_code=404, detail="User not found")

    # Fetch the existing user data from Firestore to ensure created_at is not modified
    existing_user = user_doc.to_dict()

    # Check if the email in the request body matches the email in the URL
    if user.email != email:
        raise HTTPException(status_code=400, detail="Email cannot be updated")

    # Prepare the update dictionary with the required fields only
    updated_user_data = {
        "email": existing_user["email"],  # Keep email intact (can't be updated)
        "name": user.name if user.name else existing_user["name"],  # Update name if provided
        "phone": user.phone if user.phone else existing_user["phone"],  # Update phone if provided
        "created_at": existing_user["created_at"],  # Keep created_at intact
        "updated_at": datetime.utcnow()  # Automatically update updated_at timestamp
    }

    # Update the user document in Firestore
    user_ref.update(updated_user_data)

    # Return the updated user data
    updated_user = User(
        email=updated_user_data["email"],
        name=updated_user_data["name"],
        phone=updated_user_data["phone"],
        created_at=updated_user_data["created_at"],
        updated_at=updated_user_data["updated_at"]
    )

    # Use jsonable_encoder to properly handle any complex data types (like datetime)
    return jsonable_encoder(updated_user)

# Delete User
@app.delete("/users/{email}")
async def delete_user(email: str):
    user_ref = db.collection("users").document(email)
    user_doc = user_ref.get()
    if not user_doc.exists:
        raise HTTPException(status_code=404, detail="User not found")
    user_ref.delete()
    return {"message": "User deleted successfully"}
