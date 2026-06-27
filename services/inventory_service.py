
import pandas as pd
import os

FILE_PATH = "database/spare_parts.csv"

def load_inventory():
    if os.path.exists(FILE_PATH):
        return pd.read_csv(FILE_PATH)
    return pd.DataFrame()

def save_inventory(data):
    df = load_inventory()
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)
