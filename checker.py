import requests
import hashlib
import sys


def request_api_data(hashed_password):
    # request from api with hashed password.
    url = 'https://api.pwnedpasswords.com/range/' + hashed_password
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching: {response.status_code}, check api and try again.")
    return response


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # check if password exists in api response.
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, remaining_char = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, remaining_char)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times. You should change your password.")
        else:
            print(f"{password} was not found. All good.")
    return "done!"


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))