import requests

def apod():
    url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    data = requests.get(url).json()

    print("\n🛰️ NASA APOD")
    print("-" * 40)
    print("Title:", data["title"])
    print("URL:", data["url"])
    print("Description:", data["explanation"])


def iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    data = requests.get(url).json()

    pos = data["iss_position"]

    print("\n🌍 ISS Current Location")
    print("-" * 40)
    print("Latitude:", pos["latitude"])
    print("Longitude:", pos["longitude"])


def asteroid():
    url = "https://api.nasa.gov/neo/rest/v1/feed?api_key=DEMO_KEY"
    data = requests.get(url).json()

    day = list(data["near_earth_objects"].keys())[0]
    count = len(data["near_earth_objects"][day])

    print("\n☄️ Asteroid Data")
    print("-" * 40)
    print("Date:", day)
    print("Asteroids Today:", count)


def menu():

    while True:

        print("\n===== VYTOR SPACE INTELLIGENCE v4 =====")
        print("1 - NASA APOD")
        print("2 - ISS Location")
        print("3 - Asteroid Data")
        print("0 - Exit")

        choice = input("\nSelect option: ")

        if choice == "1":
            apod()

        elif choice == "2":
            iss_location()

        elif choice == "3":
            asteroid()

        elif choice == "0":
            print("\nExiting Vytor...")
            break

        else:
            print("\nInvalid option")


menu()
