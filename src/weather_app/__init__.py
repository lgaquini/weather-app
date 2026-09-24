from .weather import get_city_data, get_city_info, print_info_user


def main() -> None:
    chosen_city: str = input("Digite o nome da sua cidade: ").strip()

    city_info = get_city_info(chosen_city)

    print_info_user(get_city_data(city_info))


if __name__ == "__main__":
    main()
