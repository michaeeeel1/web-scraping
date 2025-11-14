import requests

# Ваш API-ключ
API_KEY = "7e04c92c44b1421d94b113151250604"

# Базовый URL для запроса текущей погоды
BASE_URL = "http://api.weatherapi.com/v1/current.json"

# Параметры запроса
params = {
    "key": API_KEY,     # API-ключ
    "q": "Moscow",      # Город
    "lang": "ru"        # Язык ответа — русский
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()

    print("Город:", data["location"]["name"])
    print("Страна:", data["location"]["country"])
    print("Температура (°C):", data["current"]["temp_c"])
    print("Ощущается как (°C):", data["current"]["feelslike_c"])
    print("Погодное условие:", data["current"]["condition"]["text"])
    print("Скорость ветра (км/ч):", data["current"]["wind_kph"])
else:
    print("Ошибка при запросе:", response.status_code, response.text)