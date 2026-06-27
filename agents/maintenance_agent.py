
class MaintenanceAgent:

    def __init__(self, maintenance):
        self.maintenance = maintenance

    def upcoming_summary(self):

        total = len(self.maintenance)

        return {
            "upcoming": total,
            "message": f"{total} maintenance visits available."
        }
