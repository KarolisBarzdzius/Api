import requests
import json

preke_1={
    "pavadinimas":"kazkas1",
    "kaina":1,
    "kiekis":99.99
}

preke_2={
    "pavadinimas":"kazkas2",
    "kaina":2,
    "kiekis":9
}

preke_3={
    "pavadinimas":"kazkas3",
    "kaina":3,
    "kiekis":3333333.33333333
}

# requests.post("http://127.0.0.1:5000/preke",json=preke_1)
print(json.loads(requests.get("http://127.0.0.1:5000/preke").text))
