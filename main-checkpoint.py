# main.py

import pandas as pd
from data_fetcher import fetch_pet_data
from preprocessing import preprocess_data
from model_trainer import train_model
from predictor import predict_next_vaccine_due
import datetime

# Step 1: Fetch the data
df = fetch_pet_data()

# Step 2: Preprocess the data
X, y = preprocess_data(df)

# Step 3: Train the model
model = train_model(X, y)

# Step 4: Predict the next vaccine due date for a new pet (example)
age = 4  # years
last_vaccine_days_ago = 200  # days

# Corrected the variable name from pet_age to age
predicted_days_until_next_vaccine = predict_next_vaccine_due(model, age, last_vaccine_days_ago)
predicted_next_vaccine_date = pd.Timestamp.now() + pd.to_timedelta(predicted_days_until_next_vaccine[0], unit='D')

print(f"Predicted next vaccine date: {predicted_next_vaccine_date}")
