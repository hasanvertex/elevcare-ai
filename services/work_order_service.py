
import pandas as pd
import os

FILE_PATH = "database/work_orders.csv"

def load_work_orders():

    if os.path.exists(FILE_PATH):
        return pd.read_csv(FILE_PATH)

    return pd.DataFrame()

def save_work_order(data):

    df = load_work_orders()

    df = pd.concat(
        [df, pd.DataFrame([data])],
        ignore_index=True
    )

    df.to_csv(FILE_PATH, index=False)
