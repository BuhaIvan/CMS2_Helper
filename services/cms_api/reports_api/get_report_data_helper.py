from services.cms_api.base_cms_client import BaseClient


class GetReportDataHelper(BaseClient):
    def get_report_data(self, report_api, payload):
        headers = {
            "Authorization": f"Bearer {self.jwt_token}"
        }

        response = self.post(endpoint=report_api, payload=payload, params=None, headers=headers)

        return response.json()