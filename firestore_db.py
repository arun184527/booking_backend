import firebase_admin
from firebase_admin import credentials, firestore
import os

# Get absolute path of current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to service account key
KEY_PATH = os.path.join(BASE_DIR, "serviceAccountKey.json")

# Initialize Firebase app only once
if not firebase_admin._apps:
    cred = credentials.Certificate(KEY_PATH)
    firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()