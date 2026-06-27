
from components.contract_pie_chart import contract_pie_chart
from components.maintenance_trend import maintenance_trend
from components.technician_ranking import technician_ranking

def dashboard_analytics(
    maintenance,
    active,
    warning,
    expired
):

    contract_pie_chart(
        active,
        warning,
        expired
    )

    maintenance_trend(
        maintenance
    )

    technician_ranking()
