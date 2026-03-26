import numpy as np

# 1. TRAINING DATA (Input patterns)
# [1, 0, 0] -> Answer should be 1 (First number is 1)
# [0, 1, 1] -> Answer should be 0 (First number is 0)
inputs = np.array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]])
outputs = np.array([[0,1,1,0]]).T

# 2. THE BRAIN (Weights)
np.random.seed(1)
weights = 2 * np.random.random((3,1)) - 1

print("--- AI STARTING TRAINING ---")

# 3. THE TRAINING LOOP
for iteration in range(10000):
    input_layer = inputs
    # Activation Function (Thinking process)
    prediction = 1 / (1 + np.exp(-(np.dot(input_layer, weights))))
    
    # Error Calculation (Kitna galat tha AI)
    error = outputs - prediction
    
    # Adjustments (Galti sudharna)
    adjustments = error * (prediction * (1 - prediction))
    weights += np.dot(input_layer.T, adjustments)

print("--- TRAINING COMPLETE ---")
print("New Weights:\n", weights)

# 4. TESTING THE BRAIN
test_data = np.array([1, 0, 0])
result = 1 / (1 + np.exp(-(np.dot(test_data, weights))))
print(f"\nTesting AI with [1, 0, 0]... Prediction: {result[0]}")