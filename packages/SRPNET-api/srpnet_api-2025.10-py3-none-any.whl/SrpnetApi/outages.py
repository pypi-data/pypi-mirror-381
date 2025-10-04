import requests
from . import BASE_API_URL

API_URL = f"{BASE_API_URL}/outages"

class Outages:
    session: requests.Session = None
    xsrf_token = None
    account_id = None  # "000000000"

    def ice_reimbursement_info(self,  # account_id=None
                               ):
        # if account_id is None:
        #     account_id = self.account_id
        """

        :return: info about ice reimbursement availability
        """
        return self.session.get(url=f"{API_URL}/icereimbursementinfo",
                        #  params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def get_all_outages(self, # account_id=None
                                  ):
        # if account_id is None:
        #     account_id = self.account_id
        """
        :return: list of outages
        """
        return self.session.get(url=f"{API_URL}/getall",
                        #  params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def in_outage(self, account_id=None):
        """

        :param account_id:
        :return:  dictionary with metadata about whether the given account is in an outage.
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/userinoutage",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()
    def outage_history(self, account_id=None):
        """

        :param account_id:
        :return: dictionary contianing a list of outages in the last two years and metadata about total length of outages.
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/history",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def last_reported_outage(self, account_id=None):
        """

        :param account_id:
        :return: last reported outage by user
        """
        if account_id is None:
           account_id = self.account_id
        return self.session.get(url=f"{API_URL}/lastReportedOutage",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def outage_get_medical_support_option(self,account_id=None):
        """

        :param account_id:
        :return: bool
        """
        if account_id is None:
           account_id = self.account_id
        return self.session.get(url=f"{API_URL}/getMedicalSupportOption",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def outage_is_ineligible_to_report(self, account_id=None):
        """

        :param account_id:
        :return: bool
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/isIneligibleToReport",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()