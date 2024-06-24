# Function to store the Firebase Auth token in cookies
import streamlit_cookies_manager

class CookieManager:
    def __init__(self):
        self.cookies = streamlit_cookies_manager.CookieManager()

    def store_in_cookies(self, key, value):
        if key in self.cookies:
            del self.cookies[key]
        self.cookies[key] = value
        # self.cookies.save()

    def get_from_cookies(self, key):
        return self.cookies.get(key)

    def delete_from_cookies(self, key):
        if key in self.cookies:
            del self.cookies[key]
            # self.cookies.save()

    def save(self):
        self.cookies.save()
