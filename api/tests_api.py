# test_api.py
import requests
import json

BASE_URL = "http://127.0.0.1:8000/api"

# 1. Obtenir un token
print("=== 1. Obtenir un token ===")
response = requests.post(f"{BASE_URL}/auth/token/", json={
    "username": "api",
    "password": "1234"
})
token_data = response.json()
access_token = token_data.get('access')
print(f"Token obtenu: {access_token[:50]}...")

headers = {"Authorization": f"Bearer {access_token}"}

# 2. Lister les auteurs
print("\n=== 2. Lister les auteurs ===")
response = requests.get(f"{BASE_URL}/auteurs/", headers=headers)
print(f"Status: {response.status_code}")
print(json.dumps(response.json(), indent=2, ensure_ascii=False)[:500])

# 3. Créer un auteur
print("\n=== 3. Créer un auteur ===")
response = requests.post(f"{BASE_URL}/auteurs/", 
    headers={**headers, "Content-Type": "application/json"},
    json={"nom": "Albert Camus", "nationalite": "Française", "biographie": "Écrivain français"}
)
print(f"Status: {response.status_code}")
print(json.dumps(response.json(), indent=2, ensure_ascii=False))

# 4. Lister les livres
print("\n=== 4. Lister les livres ===")
response = requests.get(f"{BASE_URL}/livres/", headers=headers)
print(f"Status: {response.status_code}")

# 5. Créer un livre
print("\n=== 5. Créer un livre ===")
response = requests.post(f"{BASE_URL}/livres/",
    headers={**headers, "Content-Type": "application/json"},
    json={
        "titre": "L'Étranger",
        "isbn": "9782070360024",
        "annee_publication": 1942,
        "categorie": "roman",
        "auteur": 1
    }
)
print(f"Status: {response.status_code}")
print(json.dumps(response.json(), indent=2, ensure_ascii=False))

# 6. Tester la pagination
print("\n=== 6. Pagination ===")
response = requests.get(f"{BASE_URL}/livres/?page=1&size=5", headers=headers)
print(f"Status: {response.status_code}")

# 7. Tester les filtres
print("\n=== 7. Filtres ===")
response = requests.get(f"{BASE_URL}/livres/?categorie=roman&disponible=true", headers=headers)
print(f"Status: {response.status_code}")

# 8. Tester la recherche
print("\n=== 8. Recherche ===")
response = requests.get(f"{BASE_URL}/livres/?search=tranger", headers=headers)
print(f"Status: {response.status_code}")

print("\n=== Tests terminés ===")