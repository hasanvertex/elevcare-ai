import pandas as pd
from datetime import datetime


class ContractAgent:

    def __init__(self, contracts):
        self.contracts = contracts

    def expiring_contracts(self, days=30):

        today = datetime.today()

        alerts = []

        for _, row in self.contracts.iterrows():

            try:
                end_date = pd.to_datetime(
                    row["end_date"]
                )

                remaining = (
                    end_date - today
                ).days

                if 0 <= remaining <= days:

                    alerts.append({
                        "customer": row["customer_id"],
                        "days_left": remaining,
                        "end_date": row["end_date"]
                    })

            except:
                pass

        return alerts

    def expired_contracts(self):

        today = datetime.today()

        expired = []

        for _, row in self.contracts.iterrows():

            try:
                end_date = pd.to_datetime(
                    row["end_date"]
                )

                if end_date < today:

                    expired.append({
                        "customer": row["customer_id"],
                        "end_date": row["end_date"]
                    })

            except:
                pass

        return expired

    def total_contracts(self):

        return len(self.contracts)

    def active_contracts(self):

        today = datetime.today()

        count = 0

        for _, row in self.contracts.iterrows():

            try:
                end_date = pd.to_datetime(
                    row["end_date"]
                )

                if end_date >= today:
                    count += 1

            except:
                pass

        return count

    def summary(self):

        return {
            "total": self.total_contracts(),
            "active": self.active_contracts(),
            "expired": len(
                self.expired_contracts()
            ),
            "expiring": len(
                self.expiring_contracts()
            )
        }