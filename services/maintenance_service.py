import pandas as pd
import os

FILE_PATH = "database/maintenance.csv"


def load_maintenance():
    if os.path.exists(FILE_PATH):
        return pd.read_csv(FILE_PATH)
    return pd.DataFrame()


def save_maintenance(data):
    df = load_maintenance()
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)
