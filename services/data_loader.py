import pandas as pd


def load_data():

    return {
        "users": pd.read_csv("database/users.csv"),
        "customers": pd.read_csv("database/customers.csv"),
        "elevators": pd.read_csv("database/elevators.csv"),
        "contracts": pd.read_csv("database/contracts.csv"),
        "maintenance": pd.read_csv("database/maintenance.csv"),
        "technicians": pd.read_csv("database/technicians.csv"),
        "spare_parts": pd.read_csv("database/spare_parts.csv"),
        "expenses": pd.read_csv("database/expenses.csv"),
        "work_orders": pd.read_csv("database/work_orders.csv")
    }
    