import requests 
BASE_URL = "http://127.0.0.1:8000/api" 
print("=== Test de l'API ===") 
try: 
    response = requests.get(f"{BASE_URL}/livres/") 
    print(f"Statut: {response.status_code}") 
    if response.status_code == 200: 
        print("? API fonctionne !") 
except Exception as e: 
    print(f"Erreur: {e}") 
