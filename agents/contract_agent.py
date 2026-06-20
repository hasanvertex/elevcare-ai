from datetime import datetime
import pandas as pd


class ContractAgent:

    def check_contract(self, customer_id, expiry_date):

        today = datetime.today()
        expiry = datetime.strptime(expiry_date, "%m/%d/%Y")

        days_left = (expiry - today).days

        if days_left < 0:
            return f"{customer_id}: Contract has expired."

        elif days_left <= 30:
            return f"{customer_id}: Contract expires in {days_left} days. Renewal recommended."

        else:
            return f"{customer_id}: Contract is active."

    def check_contracts(self):

        contracts = pd.read_csv("database/contracts.csv")

        results = []

        for _, row in contracts.iterrows():

            result = self.check_contract(
                row["customer_id"],
                row["end_date"]
            )

            results.append(result)

        return results


if __name__ == "__main__":

    agent = ContractAgent()

    for result in agent.check_contracts():
        print(result)