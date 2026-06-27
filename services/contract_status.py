from datetime import datetime
import pandas as pd

def contract_status(contracts):

    today = datetime.today()

    active = 0
    expired = 0
    warning = 0
    alerts = []

    for _, row in contracts.iterrows():

        try:

            end_date = pd.to_datetime(
                row["end_date"]
            )

            days = (end_date - today).days

            if days < 0:
                expired += 1

            elif days <= 30:

                warning += 1

                alerts.append({
                    "Customer": row["customer_id"],
                    "Days Left": days,
                    "End Date": row["end_date"]
                })

            else:
                active += 1

        except:
            pass

    return active, warning, expired, alerts