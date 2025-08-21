import requests

class BaseClass:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
       self.header = {
           "content-type": "application/json"
       }

    def get(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self.header)
        return response
