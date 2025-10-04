import requests
from . import BASE_API_URL, accounts, autopay, documents, other, outages, payments, usage

API_URL = f"{BASE_API_URL}/login"
class Client(accounts.Account,
             autopay.Autopay,
             documents.Documents,
             other.Other,
             outages.Outages,
             payments.Payments,
             usage.Usage):
    def __init__(self,username, password, account_id=None):
        """

        :param username: SRP username; typically email
        :param password: SRP password
        :param account_id: account id for one of the accounts associated with the username, in this instance,
                            can be in the form xxx-xxx-xxx or xxxxxxxxx other uses of account ID require xxxxxxxxx
        """
        if account_id:
            if type(account_id) is str:
                self.account_id = account_id.replace('-','') # "000000000" not "000-000-000"
            else:
                self.account_id = str(account_id)
        else:
            self.account_id = None

        self.session = requests.Session()
        self.username = username
        self.password = password
        self.xsrf_token = None
        self.session_active = self.start_session()
        self.profile = None
        self.accounts = None

        if self.account_id is None:
            # if no account ID is given use get_all_accounts to find the default account
            self.get_all_accounts()

    def start_session(self):
        """
        :return: returns true if SRP successfully logged you in.
        """
        response = self.session.post(
            url=f"{API_URL}/authorize",
            data={"username": self.username, "password": self.password},
        )
        if not response.json()["message"] == "Log in successful.":
            return False
        return self.validate()

    def validate(self):
        """
        :return: Retrieves antiforgery token from SRP and stores it. Returns true if successfull
        """
        response = self.session.get(f"{API_URL}/antiforgerytoken")
        if 401 == response.status_code:
            self.session_active = False
            return False
        self.xsrf_token = response.json()["xsrfToken"]
        return self.xsrf_token is not None

    def get_profile(self):
        """
        :return: gets profile from SRP, includes info like email, address etc.
        """
        self.profile = self.session.get(f"{API_URL}/profile").json()
        return self.profile
