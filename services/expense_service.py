
import pandas as pd
import os

FILE_PATH = "database/expenses.csv"

def load_expenses():
    if os.path.exists(FILE_PATH):
        return pd.read_csv(FILE_PATH)
    return pd.DataFrame()

def save_expense(data):
    df = load_expenses()
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)
