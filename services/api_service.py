# services/api_service.py
import requests

class ApiService:
    def call_api(self):
        api_url = "https://api.example.com/data"
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return f"Error al llamar a la API: {e}"
