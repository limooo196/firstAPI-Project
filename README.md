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
3.Place the Firebase credentials .json file in the project directory (e.g., firebase_credentials.json).
4. Update the path to your Firebase credentials in the code:
```
cred = credentials.Certificate("./firebase_credentials.json")
```



Running the Application
To start the FastAPI server, run the following command:
```
uvicorn main:app --reload
```


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

