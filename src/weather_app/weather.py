from typing import Any

import requests

position_url = "https://geocoding-api.open-meteo.com/v1/search"
temperature_url = "https://api.open-meteo.com/v1/forecast"


def get_city_info(city_name: str) -> dict[str, Any]:
    """
    Get the city information based on the name.
    """
    request = requests.get(
        position_url,
        params={"name": city_name, "count": 1, "language": "pt", "format": "json"},
        timeout=10,
    )
    return request.json()


def get_city_data(city_info: dict[str, Any]):
    """
    Get the temperature data for the city, using latitude and longitude as input.
    """
    latitude = city_info["results"][0]["latitude"]
    longitute = city_info["results"][0]["longitude"]

    request = requests.get(
        temperature_url,
        params={
            "latitude": latitude,
            "longitude": longitute,
            "timezone": "auto",
            "current": "temperature_2m,relative_humidity_2m,weather_code",
        },
    )
    return request.json()


chosen_city: str = str(input("Digite o nome da sua cidade:"))

city_info = get_city_info(chosen_city)

print(get_city_data(city_info))
