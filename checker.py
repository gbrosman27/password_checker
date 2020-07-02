import requests

# request from api with hashed password (k-anonymity)
url = 'https://api.pwnedpasswords.com/range/' + 'F1CEE'
response = requests.get(url)
print(response)

