import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./pythonfastapiproject-firebase-adminsdk-fbsvc-31f940d316.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
