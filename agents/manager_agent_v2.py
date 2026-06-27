def manager_agent(question, data):

    question = question.lower()

    if "pending" in question:
        return f"Work Orders: {len(data['work_orders'])}"

    if "customer" in question:
        return f"Customers: {len(data['customers'])}"

    if "technician" in question:
        return f"Technicians: {len(data['technicians'])}"

    if "maintenance" in question:
        return f"Maintenance Records: {len(data['maintenance'])}"

    if "contract" in question:
        return f"Contracts: {len(data['contracts'])}"

    return "No information found."
