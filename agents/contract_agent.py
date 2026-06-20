from datetime import datetime

class ContractAgent:

    def check_contract(self, customer, expiry_date):

        today = datetime.today()
        expiry = datetime.strptime(expiry_date, "%Y-%m-%d")

        days_left = (expiry - today).days

        if days_left <= 30:
            return f"{customer} contract expires in {days_left} days. Renewal recommended."

        return f"{customer} contract is active."


agent = ContractAgent()

print(
    agent.check_contract(
        "ABC Tower",
        "2026-07-10"
    )
)