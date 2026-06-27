from app_pages.dashboard_page import dashboard_page
from app_pages.customers_page import customers_page
from app_pages.elevators_page import elevators_page
from app_pages.contracts_page import contracts_page
from app_pages.maintenance_page import maintenance_page
from app_pages.technicians_page import technicians_page
from app_pages.inventory_page import inventory_page
from app_pages.expenses_page import expenses_page

from app_pages.work_order_page import work_order_page
from app_pages.calendar_page import calendar_page
from app_pages.document_page import document_page
from app_pages.report_page import report_page
from app_pages.qr_page import qr_page

from app_pages.technician_dashboard_page import (
    technician_dashboard_page
)

from app_pages.manager_dashboard_page import (
    manager_dashboard_page
)

from app_pages.notification_page import (
    notification_page
)

from app_pages.ai_manager_v2_page import (
    ai_manager_v2_page
)

from app_pages.technician_mobile_page import (
    technician_mobile_page
)


def route_page(
    selected,
    data,
    active,
    warning,
    expired,
    alerts
):

    if selected == "📊 Dashboard":

        dashboard_page(
            data["customers"],
            data["elevators"],
            data["contracts"],
            data["maintenance"],
            active,
            warning,
            expired,
            alerts
        )

    elif selected == "👥 Customers":

        customers_page(
            data["customers"],
            data["elevators"],
            data["contracts"]
        )

    elif selected == "🏢 Elevators":

        elevators_page(
            data["elevators"],
            data["maintenance"]
        )

    elif selected == "📄 Contracts":

        contracts_page(
            data["contracts"]
        )

    elif selected == "🔧 Maintenance":

        maintenance_page(
            data["maintenance"]
        )

    elif selected == "👨‍🔧 Technicians":

        technicians_page(
            data["technicians"],
            data["maintenance"]
        )

    elif selected == "📦 Inventory":

        inventory_page(
            data["spare_parts"]
        )

    elif selected == "💰 Expenses":

        expenses_page(
            data["expenses"]
        )

    elif selected == "📝 Work Orders":

        work_order_page(
            data["work_orders"]
        )

    elif selected == "📅 Calendar":

        calendar_page(
            data["maintenance"]
        )

    elif selected == "📷 Documents":

        document_page()

    elif selected == "📄 Reports":

        report_page()

    elif selected == "📱 QR Codes":

        qr_page()

    elif selected == "👨‍🔧 Dashboard":

        technician_dashboard_page(
            data["technicians"],
            data["work_orders"]
        )

    elif selected == "📈 Manager Dashboard":

        manager_dashboard_page(
            data
        )

    elif selected == "🔔 Notifications":

        notification_page(
            data
        )

    elif selected == "🤖 AI Manager V2":

        ai_manager_v2_page(
            data
        )

    elif selected == "📱 Technician Mobile":

        technician_mobile_page(
            data["work_orders"]
        )