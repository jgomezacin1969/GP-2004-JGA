import requests

url = "http://127.0.0.1:5000/clasificar"
data = {
    "NUMERO_SOLICITUD": "12345",
    "TEXTO_A_CLASIFICAR": "Este es el texto que será clasificado"
}

response = requests.post(url, json=data)
print(response.json())
