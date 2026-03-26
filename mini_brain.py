import random

def pappu_ai_decision():
    # 1. Random Data Generate (Real-world simulation)
    temp = random.randint(15, 45) 
    hum = random.randint(30, 95)

    print(f"--- 🧠 PAPPU'S MASTER AI REPORT ---")
    print(f"Current Temperature: {temp}°C")
    print(f"Current Humidity: {hum}%")
    print("-" * 35)

    # 2. Advanced Logic (The Decision Maker)
    if hum > 85:
        advice = "⛈️ Tez Baarish! Ghar pe raho aur Garma-Garam PAKODE khao. ☕"
    elif 65 <= hum <= 85:
        advice = "☔ Halki Baarish ho sakti hai. CHHATRI (Umbrella) saath rakho."
    elif temp > 35:
        advice = "☀️ Bahut Garmi hai! Thanda paani piyo aur AC/Cooler chalao. 🥤"
    elif temp < 22:
        advice = "❄️ Mausam Thanda hai! Apni JACKET pehen lo, Pappu. 🧥"
    else:
        advice = "🌈 Mausam Suhana hai! Bahar ghoomne ya doston se milne jao. 🚲"

    print(f"RESULT: {advice}")
    print("-" * 35)
    print("✅ Logic Executed Successfully!")

if __name__ == "__main__":
    pappu_ai_decision()