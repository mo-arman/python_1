# pip install requests

import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # Output: 200
