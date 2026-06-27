
def get_notifications(data):

    notifications = []

    if len(data["work_orders"]) > 0:
        notifications.append(
            f"{len(data['work_orders'])} work orders available."
        )

    if len(data["maintenance"]) > 0:
        notifications.append(
            f"{len(data['maintenance'])} maintenance records."
        )

    return notifications
