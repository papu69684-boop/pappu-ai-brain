import requests
import numpy as np
from sklearn.linear_model import LinearRegression

def pappu_ml_weather_ai():
    # 1. AI ki Training ka chota sa data (Pattern Seekhne ke liye)
    # [Temperature]
    X_train = np.array([[20], [25], [30], [35], [40]]) 
    # [Humidity]
    y_train = np.array([40, 55, 70, 85, 95]) 

    # Model ko Train karo
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 2. Bhubaneswar ka LIVE data uthao
    url = "https://wttr.in/Bhubaneswar?format=j1"
    print("--- 📡 FETCHING LIVE DATA & RUNNING ML PREDICTION ---")
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            live_temp = int(data['current_condition'][0]['temp_C'])
            live_hum = int(data['current_condition'][0]['humidity'])

            # 3. AI se Prediction maango (ML Part)
            predicted_hum = model.predict([[live_temp]])[0]

            print(f"Bhubaneswar Live Temp: {live_temp}°C")
            print(f"Bhubaneswar Live Humidity: {live_hum}%")
            print(f"🤖 AI Predicted Humidity: {predicted_hum:.2f}%")
            print("-" * 45)

            # 4. Decision Logic
            diff = abs(live_hum - predicted_hum)
            if diff < 5:
                print("RESULT: AI ki prediction bilkul sahi hai! Pattern match ho gaya.")
            else:
                print("RESULT: Mausam thoda unpredictable hai, AI pattern se alag hai.")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    pappu_ml_weather_ai()