import pandas as pd
import os

FILE_PATH = "database/customers.csv"


def load_customers():
    if os.path.exists(FILE_PATH):
        return pd.read_csv(FILE_PATH)
    return pd.DataFrame()


def save_customer(customer_data):
    df = load_customers()
    df = pd.concat([df, pd.DataFrame([customer_data])], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)


def delete_customer(customer_id):
    df = load_customers()
    df = df[df["customer_id"].astype(str) != str(customer_id)]
    df.to_csv(FILE_PATH, index=False)
