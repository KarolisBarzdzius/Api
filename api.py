import requests
import json

# Įrašome užduotį:

nauja_uzduotis = {
    "pavadinimas": "Išplauti indus",
    "atlikta": False
}

r = requests.post('http://127.0.0.1:8000/uzduotis', json=nauja_uzduotis)
print(json.loads(r.text))

# Nuskaitome visas užduotis:

r = requests.get('http://127.0.0.1:8000/uzduotis')
print(json.loads(r.text))

# Nuskaitome vieną užduotį:

r = requests.get('http://127.0.0.1:8000/uzduotis/2')
print(json.loads(r.text))

# Pakeičiame vieną užduotį:

nauja_uzduotis = {
    "pavadinimas": "Išplauti grindis",
    "atlikta": False
}

r = requests.put('http://127.0.0.1:8000/uzduotis/2', json=nauja_uzduotis)
print(json.loads(r.text))

# Ištriname užduotį:

r = requests.delete('http://127.0.0.1:8000/uzduotis/1')
print(json.loads(r.text))