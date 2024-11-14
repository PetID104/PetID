import pandas as pd
from db_connect import get_db_connection

def fetch_pet_data():
    connection = get_db_connection()
    
    query = """
        SELECT pet_id, age, last_vaccine_date, next_vaccine_due
        FROM pets
    """
    
    # Fetch data from the database into a DataFrame
    df = pd.read_sql(query, connection)
    connection.close()
    
    return df

# To check if the data is fetched correctly, use this block:
if __name__ == "__main__":
    df = fetch_pet_data()
    print(df)  # This will print the DataFrame if the script is run directly
