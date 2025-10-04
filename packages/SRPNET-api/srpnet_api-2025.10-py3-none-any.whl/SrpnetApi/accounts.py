import requests
from . import BASE_API_URL
API_URL = f"{BASE_API_URL}/accounts"
class Account:
    session: requests.Session = None
    xsrf_token = None
    account_id = None  # "000000000"
    accounts = None

    def get_all_accounts(self):
        """
        Sets default account_id if none is set already
        :return: list of accounts associated with SRP power
        """
        self.accounts = (
            self.session.get(url=f"{API_URL}/all",
                             params={"includeWater": True},
                             headers={"x-xsrf-token": self.xsrf_token}).json()["billAccountList"])
        if self.account_id is None:
            self.account_id = self.accounts[0]["accountWithLeadingZeros"]

        return self.accounts

    def billing_address(self, account_id=None):
        """
        :param account_id:
        :return: billing address for associated account
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/billingaddress",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def get_account_history(self, account_id=None):
        """
        :param account_id:
        :return: list dicts of last 36 bills. Includes monthly billing data like demand, kWh usage by peak classification, etc.
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/getaccounthistory",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def get_account_manager(self, account_id=None):
        """
        :param account_id:
        :return: account manager information like if one exists and their name
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/getaccountmanager",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def get_account_address(self, account_id=None):
        """

        :param account_id:
        :return: account address for associated account as a dictionary
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/getaddress",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def get_compare_my_price_plan(self, account_id=None):
        """

        :param account_id:
        :return: returns a dictionary of a comparison between eligible price plans when possible.
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/getcomparemypriceplan",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def get_current_bill_info(self, account_id=None):
        """

        :param account_id:
        :return: bill amount for the current period since last read.
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/getcurrentbillinfo",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def get_mpower_data(self, account_id=None):
        """

        :param account_id:
        :return: dictionary of mpower data if account is currently using the mpower plan. otherwise has garbage values
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/getmpowerdata",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def get_phone(self, account_id=None):
        """

        :param account_id:
        :return: dictionary with "best phone" and "alternate phone" contacts
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/getphone",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def get_rate_code(self, account_id=None):
        """

        :param account_id:
        :return: dictionary with accounts rate plan description. Short description has the E-number. e.g. "E-27" for customer generation plan
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/getratecode",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def get_rate_metadata(self, account_id=None):
        """

        :param account_id:
        :return: dictionary similar to get_rate_code, but includes data like elap/qf-24, customer names, MPower status, demand status, etc
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/getratemetadata",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def hash_account(self, account_id=None):
        """

        :param account_id:
        :return: account as hashed by SRP
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/hashaccount",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()
