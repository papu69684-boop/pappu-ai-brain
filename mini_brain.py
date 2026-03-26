import mysql.connector

# --- 1. Database Connection Check ---
try:
    # Ye tumhare laptop par chalega
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD", # Apna password dalo
        database="GODS"
    )
    cursor = db.cursor()
    cursor.execute("SELECT temperature, humidity FROM Weather_Logs ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    temp, hum = result[0], result[1]
    print("✅ Local SQL Database se data mil gaya!")

except Exception as e:
    # Ye GitHub ke server par chalega (Jab SQL nahi milega)
    print("⚠️ Local SQL nahi mila (GitHub Server Mode). Fake data use kar raha hoon...")
    temp, hum = 32, 85  # Ye humne khud se maan liya
    print(f"Using Mock Data: Temp {temp}°C, Humidity {hum}%")

# --- 2. AI Prediction Logic ---
print("\n--- 🧠 PAPPU AI ANALYSIS ---")
if hum > 75:
    print("RESULT: ⛈️ Baarish ho sakti hai! Chhatri (Umbrella) le lo.")
else:
    print("RESULT: ☀️ Mausam saaf hai, maze karo!")

print("\nStatus: Workflow Completed Successfully!")