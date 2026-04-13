import requests
from config import BASE_URL, API_KEY

class ReqResClient:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "x-api-key": API_KEY
        })

    def login(self, email, password):
        url = f"{BASE_URL}/api/login"
        payload = {
            "email": email,
            "password": password
        }
        response = self.session.post(url, json=payload)
        print(f"URL: {url}")
        print(f"Payload: {payload}")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return response
    
    def get_users(self, page=1):
        url = f"{BASE_URL}/api/users"
        params = {"page": page}
        response = self.session.get(url, params=params)
        print(f"URL: {url}")
        print(f"Params: {params}")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return response