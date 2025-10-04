This is a python abstraction of the https://SRP.net https://srpnet.com api The interfaces here were
retrieved by logging into an account and navigating around documenting each call to https://myaccount.srpnet.com/myaccountapi/api

if you find any other interfaces, feel free to open an issue or submit a PR.

Usage:

```python
import SrpnetApi
client = SrpnetApi.Client("<USERNAME>","<PASSWORD>")
client.daily_usage_detail()
client.hourly_usage_detail(begin_date=)
client.get_rate_code()
client.usage_history_link()

```

Currently, this project will log in to start, but has no mechanism to relog if a session expires