def get_pending_jobs(work_orders):

    return work_orders[
        work_orders["status"] != "Completed"
    ]
