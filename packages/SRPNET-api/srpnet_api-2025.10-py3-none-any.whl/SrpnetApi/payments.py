import requests
from . import BASE_API_URL

API_URL = f"{BASE_API_URL}/payments"

class Payments:
    session: requests.Session = None
    xsrf_token = None
    account_id = None  # "000000000"

    def get_payment_schedules(self,  # account_id=None
                               ):
        # if account_id is None:
        #     account_id = self.account_id
        """

        :return:
        """
        return self.session.get(url=f"{API_URL}/getschedules",
                        #  params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def get_pending_payments(self, # account_id=None
                                  ):
        # if account_id is None:
        #     account_id = self.account_id
        """

        :return:
        """
        return self.session.get(url=f"{API_URL}/getpending",
                        #  params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def payment_is_custom_due_date_eligible(self, account_id=None):
        """

        :param account_id:
        :return: dictionary with "isEligable": bool
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/iscustomduedateeligible",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()
    def payment_history(self, account_id=None):
        """

        :param account_id:
        :return: list of dicts with metadata about past payments
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/historybyacct",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def bill_projection(self, account_id=None):
        """

        :param account_id:
        :return: dictionary with metadata about bill projection
        """
        if account_id is None:
           account_id = self.account_id
        return self.session.get(url=f"{API_URL}/billprojection",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def billing_option_details(self,account_id=None):
        """

        :param account_id:
        :return: dictionary with metadata about different options possibly available or enrolled in.
        """
        if account_id is None:
           account_id = self.account_id
        return self.session.get(url=f"{API_URL}/billingoptionsdetails",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def account_payment(self, account_id=None):
        """

        :param account_id:
        :return: metadata about payments
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/accountpayment",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def credit_extension_check(self,account_id=None):
        """

        :param account_id:
        :return:
        """
        if account_id is None:
           account_id = self.account_id
        return self.session.get(url=f"{API_URL}/creditextensioncheck",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def get_scheduled_payments(self, account_id=None):
        """

        :param account_id:
        :return: list of scheduled payments?
        """
        if account_id is None:
            account_id = self.account_id
        return self.session.get(url=f"{API_URL}/getscheduledbyacct",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()
