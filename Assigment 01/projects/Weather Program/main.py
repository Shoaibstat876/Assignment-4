import requests
from bs4 import BeautifulSoup

def get_weather(city):
    try:
        url = f"https://www.google.com/search?q=weather+{city.replace(' ', '+')}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        temperature = soup.find("span", class_="wob_t q8U8x").text
        condition = soup.find("span", class_="wob_dc").text
        time = soup.find("div", class_="wob_dts").text
        location = soup.find("div", class_="wob_loc").text

        print(f"\n📍 Location: {location}")
        print(f"🕒 Time: {time}")
        print(f"🌡️ Temperature: {temperature}°C")
        print(f"🌤️ Condition: {condition}\n")
        
    except Exception as e:
        print("❌ Could not retrieve weather data. Please check your internet connection or try another city.")

def main():
    print("=== 🌦️ Simple Weather App ===")
    city = input("Enter a city: ")
    get_weather(city)

if __name__ == "__main__":
    main()
