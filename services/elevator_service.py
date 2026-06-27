import pandas as pd
import os

FILE_PATH = "database/elevators.csv"


def load_elevators():
    if os.path.exists(FILE_PATH):
        return pd.read_csv(FILE_PATH)
    return pd.DataFrame()


def save_elevator(data):
    df = load_elevators()
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)
