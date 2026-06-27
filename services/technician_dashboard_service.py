
def get_summary(technicians, work_orders):

    total_technicians = len(technicians)
    total_orders = len(work_orders)

    completed = len(
        work_orders[
            work_orders["status"] == "Completed"
        ]
    )

    pending = total_orders - completed

    return (
        total_technicians,
        total_orders,
        completed,
        pending
    )
