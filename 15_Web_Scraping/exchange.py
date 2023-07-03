# import requests

# api_url = 'http://api.exchangeratesapi.io/v1/latest'
# access_key = 'XXXXXXXXXXXXXXXX'

# bozulan_doviz = input("Bozulan döviz cinsi: ")
# alınan_doviz = input("Alınan döviz cinsi: ")
# miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

# params = {
#     'access_key': access_key,
#     'base': bozulan_doviz,
#     'symbols': alınan_doviz
# }

# response = requests.get(api_url, params=params)
# data = response.json()

# print(data)

import requests

# API anahtarınızı buraya girin
api_key = "XXXXXXXXXXXXXXX"

# API URL'sini oluşturun
base_url = "https://api.exchangeratesapi.io/v1/latest"
params = {
    "access_key": api_key,
    "base": "EUR",  # Giriş miktarının Euro cinsinden olduğunu varsayalım
    "symbols": "USD"  # Dönüştürmek istediğiniz para birimi
}

# API isteğini gönderin
response = requests.get(base_url, params=params)

# API yanıtını kontrol edin
if response.status_code == 200:
    data = response.json()
    if data["success"]:
        rate = data["rates"]["USD"]
        amount = 100  # Giriş miktarını buraya girin
        converted_amount = amount * rate
        print(f"{amount} EUR, {converted_amount} USD'ye eşittir.")
    else:
        print("API yanıtı başarısız oldu.")
else:
    print("API isteği başarısız oldu.")

