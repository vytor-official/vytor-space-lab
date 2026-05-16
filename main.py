import requests

print("🛰️ Vytor Space Lab v2 Initializing...\n")

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

try:
    response = requests.get(url)
    data = response.json()

    print("📡 TODAY'S SPACE DATA")
    print("-" * 30)
    print("📌 Title:", data["title"])
    print("\n🧠 Description:", data["explanation"])
    print("\n🖼️ Image URL:", data["url"])

except Exception as error:
    print("❌ An error occurred:", error)
