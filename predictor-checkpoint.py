# predictor.py

import numpy as np
from model_trainer import train_model

def predict_next_vaccine_due(model, age, last_vaccine_days_ago):
    new_pet_data = np.array([[age, last_vaccine_days_ago]])
    predicted_days_until_next_vaccine = model.predict(new_pet_data)
    return predicted_days_until_next_vaccine
