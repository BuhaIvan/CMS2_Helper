from services.cms_api.reports_api.cashflow_trailers_report import CashflowTrailersReportApi


def get_late_and_shipped_orders_ids():
    start_time = input("Please enter a start time: ")
    end_time = input("Please enter a end time: ")

    cashflow_report = CashflowTrailersReportApi()
    cashflow_report.get_late_and_order_shipped_orders_ids_for_selected_month(start_time, end_time)

get_late_and_shipped_orders_ids()