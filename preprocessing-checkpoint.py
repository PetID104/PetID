# preprocessing.py

import pandas as pd

def preprocess_data(df):
    # Convert date columns to datetime
    df['last_vaccine_date'] = pd.to_datetime(df['last_vaccine_date'])
    df['next_vaccine_due'] = pd.to_datetime(df['next_vaccine_due'])
    
    # Create feature columns
    df['last_vaccine_days_ago'] = (pd.Timestamp.now() - df['last_vaccine_date']).dt.days
    df['next_vaccine_days_from_now'] = (df['next_vaccine_due'] - pd.Timestamp.now()).dt.days
    
    # Drop rows with missing values
    df = df.dropna(subset=['last_vaccine_days_ago', 'next_vaccine_days_from_now'])
    
    return df[['age', 'last_vaccine_days_ago']], df['next_vaccine_days_from_now']
    
    print(df)  # To check if df contains the expected columns and rows after preprocessing
    return df[['age', 'last_vaccine_days_ago']], df['next_vaccine_days_from_now']

