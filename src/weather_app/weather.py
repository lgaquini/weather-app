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


def get_city_data(city_info: dict[str, Any]) -> dict[str, Any]:
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
        timeout=10,
    )
    return request.json()


def print_info_user(data: dict[str, Any]):
    print(
        "TEMPERATURA: ",
        data["current"]["temperature_2m"],
        data["current_units"]["temperature_2m"],
    )


chosen_city: str = input("Digite o nome da sua cidade:").strip()

city_info = get_city_info(chosen_city)

print_info_user(get_city_data(city_info))
