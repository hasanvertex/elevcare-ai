from datetime import datetime
import pandas as pd


def get_today_visits(data):

    today = datetime.today().strftime("%m/%d/%Y")

    return data[
        data["visit_date"] == today
    ]


def get_upcoming_visits(data):

    df = data.copy()

    df["visit_date"] = pd.to_datetime(
        df["visit_date"],
        format="%m/%d/%Y",
        errors="coerce"
    )

    today = pd.Timestamp.today()

    df = df[
        df["visit_date"] >= today
    ]

    return df.sort_values(
        "visit_date"
    ).head(10)


def get_overdue_visits(data):

    df = data.copy()

    df["visit_date"] = pd.to_datetime(
        df["visit_date"],
        format="%m/%d/%Y",
        errors="coerce"
    )

    today = pd.Timestamp.today()

    return df[
        df["visit_date"] < today
    ]