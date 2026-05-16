import requests

def get_apod():
    url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    data = requests.get(url).json()

    print("\n🛰️ NASA Astronomy Picture of the Day")
    print("-" * 40)
    print("Title:", data["title"])
    print("URL:", data["url"])
    print("Description:", data["explanation"])


def menu():
    print("\n===== VYTOR SPACE LAB v3 =====")
    print("1 - NASA APOD")
    print("0 - Exit")

    choice = input("Select option: ")

    if choice == "1":
        get_apod()
    elif choice == "0":
        print("Exiting Vytor...")
    else:
        print("Invalid choice")


while True:
    menu()
