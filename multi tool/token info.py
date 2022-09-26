import requests
import random


headers = {
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50",
    "authorization": "ODIzMzQ1NDQ2MzA2OTcxNzA5.YFfeUA.mxDHi7QBJDHgjQbAQKvRIaBXT9s"
}
result = requests.get(f'https://discord.com/api/v8/users/@me/guilds', headers=headers)
print(result.status_code)
print(result.json())

# 200 good
# 403 verify
# 401 invalid