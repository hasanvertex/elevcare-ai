from contract_agent import ContractAgent
from maintenance_agent import MaintenanceAgent


contract_agent = ContractAgent()
maintenance_agent = MaintenanceAgent()

print("\n========== ELEVCARE AI ==========\n")

print("CONTRACT STATUS:")
for item in contract_agent.check_contracts():
    print("-", item)

print("\nMAINTENANCE STATUS:")
for item in maintenance_agent.check_visits():
    print("-", item)