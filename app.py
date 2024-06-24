import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
import pyrebase
from firebase_admin import firestore 
import requests
import uuid
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from utils.cookie_manager import CookieManager
from components.onboarding import needs_onboarding, show_onboarding
from config.general_config import firebaseConfig, get_auth_client, get_db, get_firebase, get_auth

st.set_page_config(page_title="Gift App", page_icon="🎁")
cookie_manager = CookieManager()

auth = get_auth()
db = get_db()
auth_client = get_auth_client()
firebase = get_firebase()

def login_page():
    st.title("Login")
    choice = st.selectbox("Login or Sign Up", ["Login", "Sign Up"])

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if choice == "Login":
        if st.button("Login"):
            try:
                user = auth_client.sign_in_with_email_and_password(email, password)
                st.success("Login successful.")
                print(user)
                user_token = user.get('idToken')

                cookie_manager.store_in_cookies('token', user_token)                    
                cookie_manager.store_in_cookies('user_id', user.get('localId'))
                cookie_manager.save()
                
                # st.session_state['user_id'] = user.get('localId')
                

                st.experimental_rerun()
            except Exception as e:
                st.error(f"Login failed: {e}")
    else:
        if st.button("Sign Up"):
            try:
                user = auth_client.create_user_with_email_and_password(email, password)
                st.success("Account created successfully.")
            except Exception as e:
                st.error(f"Sign Up failed: {e}")

    st.markdown("### Or login with Google")
    if st.button("Login with Google"):
        login_url = generate_google_login_url()
        st.markdown(f"[Click here to login with Google]({login_url})")

def generate_google_login_url():
    google_auth_endpoint = "https://accounts.google.com/o/oauth2/v2/auth"
    redirect_uri = "http://localhost:8501"
    client_id = "505194637297-dk7fl2c4m53sv1c663ha1ljhffo84rns.apps.googleusercontent.com"

    auth_url = f"{google_auth_endpoint}?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope=email%20profile&access_type=offline"
    return auth_url

def generate_uid():
    #generate valid uuid
    return uuid.uuid4()



def handle_google_auth_response():
    query_params = st.query_params
    if "code" in query_params:
        code = query_params["code"][0]
        token_url = "https://oauth2.googleapis.com/token"
        redirect_uri = "http://localhost:8501"
        client_id = "505194637297-dk7fl2c4m53sv1c663ha1ljhffo84rns.apps.googleusercontent.com"
        client_secret = "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"

        token_data = {
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code"
        }

        token_response = requests.post(token_url, data=token_data)
        token_info = token_response.json()

        if "id_token" in token_info:
            id_token_value = token_info["id_token"]
            try:
                # Verify the Google ID token
                request = google_requests.Request()
                id_info = id_token.verify_oauth2_token(id_token_value, request, client_id)
                
                # Create a custom token for the user
                custom_token = firebase_admin.auth.create_custom_token(id_info['sub'])
                
                # Sign in with the custom token
                user = auth_client.sign_in_with_custom_token(custom_token.decode('utf-8'))
                user_info = auth_client.get_account_info(user['idToken'])
                user_id = user_info.get('users')[0].get('localId')
                st.session_state['user_id'] = user_info.get('users')[0].get('localId')
                cookie_manager.store_in_cookies('user_id', user_info.get('users')[0].get('localId'))


                if cookie_manager.get_from_cookies('user_id') == user_info.get('users')[0].get('localId'):
                    if cookie_manager.get_from_cookies('token') == user['idToken']:
                        pass
                    else:
                        cookie_manager.store_in_cookies('token', user['idToken'])
                else:                    
                    cookie_manager.store_in_cookies('user_id', user_id)
                
                cookie_manager.save()

                # Store the user email in session state
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Authentication failed: {e}")
        else:
            st.error("Failed to obtain token.")
# Main Page
def main_page():
    user_id = cookie_manager.get_from_cookies('user_id')
    token = cookie_manager.get_from_cookies('token')

    if token:
        try:
            user = auth.verify_id_token(token)
            st.title("Main Page")
            if needs_onboarding(user_id):
                show_onboarding(user_id)
            else:
                st.write("Welcome back! You have already completed the onboarding.")
        except auth.InvalidIdTokenError:
            st.error("Invalid or expired token. Please log in again.")
            cookie_manager.delete_from_cookies('token')
            cookie_manager.delete_from_cookies('user_id')
            cookie_manager.save()

        

        if st.button("Logout"):
            cookie_manager.delete_from_cookies('token')
            cookie_manager.delete_from_cookies('user_id')
            cookie_manager.save()
            st.experimental_rerun()
    else:
        login_page()
        handle_google_auth_response()

# App
def main():
    

    # if 'user' not in st.session_state:
    #     st.session_state['user'] = None
    main_page()

if __name__ == "__main__":
    main()