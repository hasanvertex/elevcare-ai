def get_manager_summary(data):

    return {
        "customers": len(data["customers"]),
        "elevators": len(data["elevators"]),
        "contracts": len(data["contracts"]),
        "maintenance": len(data["maintenance"]),
        "technicians": len(data["technicians"]),
        "work_orders": len(data["work_orders"])
    }
