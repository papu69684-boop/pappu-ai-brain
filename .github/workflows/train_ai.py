import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# 1. AI ki Training ka Data (Past Weather)
# Maan lo ye pichle kuch dinon ka data hai: [Temperature]
X = np.array([[20], [25], [30], [35], [40]]) 
# Uske hisaab se [Humidity]
y = np.array([40, 55, 70, 85, 95]) 

# 2. Model ko Create aur Train karo
model = LinearRegression()
model.fit(X, y) # Yahan AI "Seekh" raha hai patterns

def predict_weather(current_temp):
    # 3. AI se Prediction maango
    prediction = model.predict([[current_temp]])
    return prediction[0]

if __name__ == "__main__":
    temp_input = 32
    result = predict_weather(temp_input)
    print(f"--- 🤖 PAPPU ML BRAIN ---")
    print(f"Agar Temp {temp_input}°C hai, toh AI ke hisaab se Humidity {result:.2f}% hogi!")