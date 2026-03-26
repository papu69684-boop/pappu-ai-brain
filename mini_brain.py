import mysql.connector

try:
    # 1. Database Connection (Bridge banana)
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD", # <-- Yahan apna asli SQL password dalo
        database="GODS"
    )
    cursor = conn.cursor()

    # 2. SQL Query (Data nikalna)
    cursor.execute("SELECT temperature, humidity, rain_occurred FROM Weather_Logs ORDER BY id DESC")
    all_data = cursor.fetchall()

    # 3. Processing (AI Analysis)
    print("--- 🧠 PAPPU AI BRAIN ANALYSIS ---")
    latest_entry = all_data[0] # Sabse naya data point
    temp, hum, rain = latest_entry
    
    print(f"Current Stats: Temp {temp}°C | Humidity {hum}%")

    # 4. Prediction Logic (Decision Making)
    if hum > 75:
        print("\n[RESULT]: ⛈️ High chance of rain! Pappu, Umbrella (Chhatri) saath rakhna.")
    else:
        print("\n[RESULT]: ☀️ Weather looks clear. No umbrella needed!")

    conn.close()

except Exception as e:
    print(f"❌ Connection Error: {e}")