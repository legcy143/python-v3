import tensorflow as tf
from tensorflow import keras
import numpy as np

# Generate sample data
X = np.random.rand(100, 1)
y = X * 2 + 1  # Simple equation: y = 2x + 1

# Build a simple AI model (Neural Network)
model = keras.Sequential([
    keras.layers.Dense(1, input_shape=(1,))
])

# Compile and train
model.compile(optimizer="adam", loss="mse")
model.fit(X, y, epochs=100, verbose=0)

# Predict with AI
print(model.predict([[0.5]]))  # Should be close to 2
