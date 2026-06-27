import pandas as pd
import os

FILE_PATH = "database/contracts.csv"


def load_contracts():
    if os.path.exists(FILE_PATH):
        return pd.read_csv(FILE_PATH)
    return pd.DataFrame()


def save_contract(contract_data):
    df = load_contracts()
    df = pd.concat([df, pd.DataFrame([contract_data])], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)
