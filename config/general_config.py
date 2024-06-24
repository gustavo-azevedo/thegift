import firebase_admin
from firebase_admin import credentials, auth
import pyrebase
from firebase_admin import firestore 

firebaseConfig = {
        "apiKey": "AIzaSyCBqbYP2izQkBYFJGvbl5OlG3LPOmfLZSI",
        "authDomain": "thegift-ad01d.firebaseapp.com",
        "databaseURL": "https://thegift-ad01d-default-rtdb.firebaseio.com",
        "projectId": "thegift-ad01d",
        "storageBucket": "thegift-ad01d.appspot.com",
        "messagingSenderId": "267694872929",
        "appId": "1:267694872929:web:cf914badd17f9bee36cd20",
        "measurementId": "G-KTKJZ2BBP2"
}

if not firebase_admin._apps:
    cred = credentials.Certificate('./firebase/key.json')
    fireabase = firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(firebaseConfig)
auth_client = firebase.auth()

db = firestore.client()

def get_db():
    return db

def get_auth_client():
    return auth_client

def get_firebase():
    return firebase

def get_auth() :
    return auth