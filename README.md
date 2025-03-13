# FastAPI Firebase User Management

This is a FastAPI project that integrates with Firebase Firestore to manage user data. The API allows performing CRUD (Create, Read, Update, Delete) operations for user management.

## Features

- **Create a user**: Add new users to Firestore.
- **Read a user**: Fetch user details by email.
- **Read all users**: Fetch a list of all users in the Firestore collection.
- **Update a user**: Modify the user's name or phone number.
- **Delete a user**: Remove a user from the Firestore database.

## Setup

### Prerequisites

- Python 3.7 or later
- Firebase Project with Firestore enabled
- Firebase Admin SDK credentials

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/fastapi-firebase-user-management.git
   ```

2. Navigate into the project directory:
  ```
cd fastapi-firebase-user-management
```

3. Create and activate a virtual environment:
```
python -m venv venv
```

# For Windows
``` 
venv\Scripts\activate
```
# For macOS/Linux
```
source venv/bin/activate
```

4. Install the required dependencies:
```
pip install -r requirements.txt
```


Firebase Setup

1.Set up Firebase and enable Firestore.

2. Create a Firebase service account and download the private key as a .json file.
3. 
3.Place the Firebase credentials .json file in the project directory (e.g., firebase_credentials.json).

5. Update the path to your Firebase credentials in the code:

```
cred = credentials.Certificate("./firebase_credentials.json")
```



Running the Application
To start the FastAPI server, run the following command:
```
uvicorn main:app --reload
```


Summary of Validations:
1. **Name**:
    
    - Must contain only letters and spaces.
    - Minimum length: 1, Maximum length: 50.
2. **Email**:
    
    - Must be in a valid email format.
    - Leading/trailing spaces are trimmed.
3. **Phone**:
    
    - Must follow international phone number format (e.g., `+6281234567890`).
    - Must have at least 10 digits.
4. **Timestamps**:
    
    - `created_at` and `updated_at` are automatically set by the server and cannot be updated by the user.
5. **Request-Level Validations**:
    
    - Ensure that the user with the provided email doesn’t already exist (`POST`).
    - Prevent users from updating their email (`PUT`).
    - Handle cases where the user does not exist (`GET`, `PUT`, `DELETE`).
  



Dependencies
FastAPI: Web framework for building APIs.
Uvicorn: ASGI server to run the FastAPI app.
firebase-admin: Firebase Admin SDK for interacting with Firestore.
Pydantic: Data validation and settings management.


License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Feel free to fork this repository and submit pull requests with improvements. Please ensure that any contributions adhere to the coding standards and follow the existing code style.

Acknowledgements
FastAPI for building high-performance APIs.
Firebase for providing scalable backend services.

