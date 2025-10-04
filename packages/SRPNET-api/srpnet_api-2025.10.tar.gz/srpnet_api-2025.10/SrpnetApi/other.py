import requests
from . import BASE_API_URL

API_URL = f"{BASE_API_URL}"

class Other:
    session: requests.Session = None
    xsrf_token = None
    account_id = None  # "000000000"

    def get_bank_accounts(self,  # account_id=None
                               ):
        # if account_id is None:
        #     account_id = self.account_id
        """

        :return: list of bank accounts associated with this account.
        """
        return self.session.get(url=f"{API_URL}/bankaccount/getlist",
                        #  params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def get_landlord_agreements(self, # account_id=None
                                  ):
        # if account_id is None:
        #     account_id = self.account_id
        """
        :return: list of landlord agreements associated with this account.
        """
        return self.session.get(url=f"{API_URL}/landlord/list",
                        #  params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()["landlordAgreements"]

    def get_notifications(self, account_id=None):
        """

        :param account_id:
        :return: dictionary of notificiation types available and subscribed which are lists of notifications.
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/notification/getnotifications",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()
    def get_primary_contacts(self, account_id=None):
        """

        :param account_id:
        :return:
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/primarycontacts/getprimarycontactinfostatus",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def wattplan_has_enough_history(self, account_id=None):
        """

        :param account_id:
        :return: dictionary describing wattplan links and available history
        """
        if account_id is None:
           account_id = self.account_id
        return self.session.get(url=f"{API_URL}/wattplan/hasenoughhistory",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

