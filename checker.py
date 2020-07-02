import requests
import hashlib


def request_api_data(hashed_password):
    # request from api with hashed password.
    url = 'https://api.pwnedpasswords.com/range/' + hashed_password
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching: {response.status_code}, check api and try again.")
    return response

def pwned_api_check(password):
    # check if password exists in API repsonse.
    # sha1password = hashlib.sha1(password.encode(utf-8))
    pass

request_api_data('123')