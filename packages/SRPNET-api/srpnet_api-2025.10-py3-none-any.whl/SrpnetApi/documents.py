import requests

import SrpnetApi
from . import accounts, BASE_API_URL


API_URL = f"{BASE_API_URL}/documents"

class Documents:
    session: requests.Session = None
    xsrf_token = None
    account_id = None  # "000000000"

    def energy_scorecard_links(self, account_id=None):
        """
        depreciated as far as I can tell

        :param account_id:
        :return:
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/energyscorecardlinks",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()
    def community_solar_link(self, account_id=None):
        """
        depreciated as far as I can tell
        :param account_id:
        :return:
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/communitysolarlink",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def ebill_list(self, account_id=None):
        """

        :param account_id:
        :return: list of dictionaries of bill id's. Used for retrieving PDF's
        """
        if account_id is None:
           account_id = self.account_id
        return self.session.get(url=f"{API_URL}/eBillList",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()["documentList"]

    def energy_scorecard_faq_link(self, # account_id=None
                                  ):
        # if account_id is None:
        #     account_id = self.account_id
        """

        :return:
        """
        return self.session.get(url=f"{API_URL}/energyscorecardfaqlink",
                        #  params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def usage_history_link(self, account_id=None, is_mpower=None):
        """

        :param account_id:
        :param is_mpower:
        :return: link to document that provides a summary of monthly usage data.
        """
        if account_id is None:
           account_id = self.account_id
        if is_mpower is None and isinstance(self,SrpnetApi.accounts.Account):
            is_mpower = self.get_rate_metadata(account_id)["isMPower"]
        return self.session.get(url=f"{API_URL}/usagehistorylink",
                         params={"billAccount": account_id,"isMPower": is_mpower},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def credit_history_link(self, account_id=None):
        """

        :param account_id:
        :return: link to document that provides a summary of monthly credit data.
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/credithistorylink",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()