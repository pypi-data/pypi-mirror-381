import requests
import datetime
from . import BASE_API_URL

API_URL = f"{BASE_API_URL}/usage"

class Usage:
    session: requests.Session = None
    xsrf_token = None
    account_id = None  # "000000000"

    def daily_weather(self,
                      # account_id=None
                      ):
        """

        :return: last 2 years of daily weather as collected by SRP
        """
       # if account_id is None:
       #     account_id = self.account_id
        return self.session.get(url=f"{API_URL}/dailyweather",
       #                  params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()
    def hourly_usage_detail(self, account_id=None,
                            begin_date: (datetime.date|str) =None,
                            end_date: (datetime.date|str) =None):
        """

        :param account_id: account id in the form (xxxxxxxxx) not (xxx-xxx-xxx)
        :param begin_date: string in ISO 8601 format or datetime.date no earlier than 1 month before end_date
                            begin_date earlier htan 1 month before end_date will result in truncated results
        :param end_date:string in ISO 8601 format or datetime.date after begin_date
        :return: list of dicts containing each hour of usage in as much as one month of time.
        """
        if end_date is None:
            end_date = datetime.date.today()
        if begin_date is None:
            begin_date = datetime.date(year=end_date.year -(1 if end_date.month==1 else 0),
                                       month=end_date.month+(-1 if end_date.month!=1 else 11),
                                       day=end_date.day)
        if account_id is None:
            account_id = self.account_id

        if not isinstance(end_date, datetime.date):
            end_date = datetime.date.fromisoformat(end_date)
        if not isinstance(begin_date, datetime.date):
            begin_date = datetime.date.fromisoformat(begin_date)

        return self.session.get(url=f"{API_URL}/hourlydetail",
                         params={"billAccount": account_id,
                                 "beginDate": begin_date.strftime("%m-%d-%Y"),
                                 "endDate": end_date.strftime("%m-%d-%Y")},
                         headers={"x-xsrf-token": self.xsrf_token}).json()

    def daily_usage_detail(self, account_id=None):
        """

        :param account_id: account id in the form (xxxxxxxxx) not (xxx-xxx-xxx) if none given,
        defaults to self.account_id
        :return: daily usage of power for account_id
        """
        if account_id is None:
           account_id = self.account_id
        return self.session.get(url=f"{API_URL}/dailyusagedetail",
                         params={"billAccount": account_id},
                         headers={"x-xsrf-token": self.xsrf_token}).json()
