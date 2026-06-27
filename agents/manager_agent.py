class ManagerAgent:

    def __init__(
        self,
        customers,
        elevators,
        contracts,
        maintenance
    ):
        self.customers = customers
        self.elevators = elevators
        self.contracts = contracts
        self.maintenance = maintenance

    def summary(self):

        return {
            "customers": len(self.customers),
            "elevators": len(self.elevators),
            "contracts": len(self.contracts),
            "maintenance": len(self.maintenance)
        }
