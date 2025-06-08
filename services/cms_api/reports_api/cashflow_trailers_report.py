from configs.constans import BASE_API_URL
from services.cms_api.reports_api.get_report_data_helper import GetReportDataHelper


class CashflowTrailersReportApi(GetReportDataHelper):
    _REPORT_API = f"{BASE_API_URL}reports/cashflow-trailers-report"

    @staticmethod
    def create_payload(
            date_from: str,
            date_to: str,
            try_get_archive: bool = True,
            reporters: list = None,
            offices: list = None,
            provinces: list = None
    ) -> dict:
        payload = {
            "asFile":False,
            "tryGetArchive":try_get_archive,
            "range":{
                "from":date_from,
                "to":date_to
            },
            "sortingField":"Created",
            "isSortDescending":True,
            "paging":{
                "skip":0,
                "take":10000
            },
            "offices":offices,
            "reporters":reporters,
            "provinces":provinces
        }
        return payload

    def get_late_and_order_shipped_orders_ids_for_selected_month(self, date_from: str, date_to: str):
        date_from = date_from + "T00:00:00.000Z"
        date_to = date_to + "T23:59:59.999Z"

        data = self.get_report_data(report_api=self._REPORT_API, payload=self.create_payload(date_from, date_to))
        list_of_items = data["items"]

        for item in list_of_items:
            if item["discountType"] == 5 or item["discountType"] == 1:
                print(item["id"])
        return self