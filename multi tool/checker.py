import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time

with open('testtokens.txt', 'r') as f:
    token_list = [token.strip() for token in f]
discord = "https://discordapp.com/api/v8/users/@me/guilds"
def checker(token):
    headers = {
            "content-type": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50",
            "authorization": token
        }
    result = requests.get(discord, headers=headers).status_code
    if result == 200:
        return {token: 0}
    elif result == 403:
        return {token: 1}
    elif result == 401:
        return {token: 2}

start = time()

with ThreadPoolExecutor(max_workers=len(token_list)) as executor:
    processes = [executor.submit(checker, token) for token in token_list]
verified_list = []
unverified_list = []
invalid_list = []
for task in as_completed(processes):
    token = list(task.result().keys())[0]
    status = list(task.result().values())[0]
    if status == 0:
        verified_list.append(token)
    elif status == 1:
        unverified_list.append(token)
    elif status == 2:
        invalid_list.append(token)


print(f'Checked {len(token_list)} tokens in {round(float(time() - start), 1)} seconds')
print(f"{len(verified_list)} worked\n{len(unverified_list)} unverified\n{len(invalid_list)} invalid")