BASE_API_URL = "https://myaccount.srpnet.com/myaccountapi/api"
__all__=[
    "client",
    "BASE_API_URL",
]
"""
Client is really the only file meant to be imported and used externally.
"""
from SrpnetApi.client import Client