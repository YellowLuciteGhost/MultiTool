import requests
import json

headers = {
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50"
}
data = json.dumps({"email": "awesomelaptop@gmail.com", "password": "7387086a"})
res = requests.post("https://discordapp.com/api/v8/auth/login", headers=headers, data=data).json()
print(res)