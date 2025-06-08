import os

from dotenv import load_dotenv

load_dotenv()

# CMS
BASE_UI_URL = "https://tcms.lgfgfashionhouse.com/#/"
BASE_API_URL = "https://cms.lgfgfashionhouse.com/api/"
SUBMIT_PAYMENT_TABLE = "https://testcms.lgfgfashionhouse.com/#/SubmitPayment/List"
DEFAULT_TIMEOUT = 10

USERNAME = os.getenv("USERNAME_")
PASSWORD = os.getenv("PASSWORD_")