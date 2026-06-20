import pandas as pd


class MaintenanceAgent:

    def check_visits(self):

        visits = pd.read_csv(
            "database/maintenance.csv"
        )

        results = []

        for _, row in visits.iterrows():

            results.append(
                f"{row['visit_date']} | "
                f"Elevator {row['elevator_id']} | "
                f"{row['technician']} | "
                f"{row['remarks']}"
            )

        return results


if __name__ == "__main__":

    agent = MaintenanceAgent()

    for result in agent.check_visits():
        print(result)