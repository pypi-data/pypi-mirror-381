import requests
from . import BASE_API_URL
API_URL = f"{BASE_API_URL}/autopay"

class Autopay:
    session: requests.Session = None
    xsrf_token = None
    account_id = None  # "000000000"

    def autopay_eligible(self, account_id=None):
        """

        :param account_id:
        :return: bool
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/getiseligible",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()
    def autopay_enrolled(self, account_id=None):
        """
        :param account_id:
        :return: bool
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/getisenrolled",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def autopay_info_list(self,
                         # account_id=None
                          ):
        # if account_id is None:
        #    account_id = self.account_id
        """

        :return: list of dicts of accounts, associated billing mechanisms and autopay eligibility and enrollment.
        """
        return self.session.get(url=f"{API_URL}/getautopayinfolist",
                         # params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def autopay_info(self, account_id=None):
        """

        :param account_id:
        :return: same dictionary as info_list but only for a single account.
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/getautopayinfo",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()
