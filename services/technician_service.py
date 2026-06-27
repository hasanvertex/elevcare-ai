import pandas as pd
import os

FILE_PATH = "database/technicians.csv"


def load_technicians():
    if os.path.exists(FILE_PATH):
        return pd.read_csv(FILE_PATH)
    return pd.DataFrame()


def save_technician(data):
    df = load_technicians()
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)
