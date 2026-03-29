import requests

def get_pappu_weather_live():
    # Bhubaneswar ka live data bina kisi account/key ke!
    url = "https://wttr.in/Bhubaneswar?format=j1"
    
    print("--- 📡 FETCHING LIVE WEATHER FOR BHUBANESWAR ---")
    
    try:
        response = requests.get(url)
        # Agar response sahi hai (Status 200)
        if response.status_code == 200:
            data = response.json()
            
            # Asli data nikalna
            current = data['current_condition'][0]
            temp = int(current['temp_C'])
            hum = int(current['humidity'])
            desc = current['weatherDesc'][0]['value']
            
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {hum}%")
            print(f"Condition: {desc}")
            print("-" * 40)
            
            # --- Pappu AI Decision Logic ---
            if hum > 80:
                advice = "⛈️ Tez Baarish ke chances! Garma-garam PAKODE ka intezam karo."
            elif temp > 35:
                advice = "☀️ Garmi zyada hai! Thanda paani piyo aur AC on karo."
            elif temp < 22:
                advice = "❄️ Mausam thanda hai! Jacket nikal lo, Pappu."
            else:
                advice = "🌈 Mausam ek dum mast hai! Bahar ghoomne jao."
                
            print(f"AI ADVICE: {advice}")
            
        else:
            print("❌ Error: Data fetch nahi ho paya.")
            
    except Exception as e:
        print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    get_pappu_weather_live()