from src.valorantapi import ValorantApi


if __name__ == "__main__":
    valorant = ValorantApi()
    buddies = valorant.get_buddies()
    print(buddies)