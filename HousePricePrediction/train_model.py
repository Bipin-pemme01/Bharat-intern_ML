import pandas as pd
from sklearn.linear_model import LinearRegression # type: ignore
import pickle

# Load dataset
df = pd.read_csv("Housing.csv")

# Simple encoding (adjust if needed)
df['mainroad'] = df['mainroad'].map({'yes': 1, 'no': 0})
df['guestroom'] = df['guestroom'].map({'yes': 1, 'no': 0})
df['furnishingstatus'] = df['furnishingstatus'].map({'unfurnished': 0, 'semi-furnished': 1, 'furnished': 2})

# Features
X = df[['area', 'bedrooms', 'bathrooms', 'stories', 'parking']]
y = df['price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
