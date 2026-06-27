from agents.contract_agent import ContractAgent
from agents.manager_agent import ManagerAgent
from services.contract_status import contract_status


def create_services(data):

    active, warning, expired, alerts = contract_status(
        data["contracts"]
    )

    manager = ManagerAgent(
        data["customers"],
        data["elevators"],
        data["contracts"],
        data["maintenance"]
    )

    contract_agent = ContractAgent(
        data["contracts"]
    )

    return (
        manager,
        contract_agent,
        active,
        warning,
        expired,
        alerts
    )
