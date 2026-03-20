import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

# Create folder if not exists
os.makedirs("model", exist_ok=True)

# Dummy dataset
data = {
    "class_size": [20, 30, 40, 50],
    "student_score": [80, 70, 60, 50],
    "teacher_effectiveness": [90, 75, 60, 50]
}

df = pd.DataFrame(data)

X = df[["class_size", "student_score"]]
y = df["teacher_effectiveness"]

model = LinearRegression()
model.fit(X, y)

# Save model correctly
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved correctly!")