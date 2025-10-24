import firebase_admin
from firebase_admin import credentials, auth
import os

def initialize_firebase():
    if not firebase_admin._apps:
        cred_path = os.path.join(os.getcwd(), "firebase_credentials.json")
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
        print("✅ Firebase initialized successfully!")

def create_user(email, password):
    """Create a new user in Firebase"""
    user = auth.create_user(email=email, password=password)
    return user

def get_user(uid):
    """Get user info by UID"""
    return auth.get_user(uid)