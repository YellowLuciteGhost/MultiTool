import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time


with open('bruhhh.txt', 'r') as f:
    token_list = [token.strip() for token in f]
discord = "https://discord.com/api/v8/invites/tCA7ZVSc87"
def checker(token):
    headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "authorization": token
    }
    result = requests.post(discord, headers=headers).json()
    return result

start = time()

with ThreadPoolExecutor(max_workers=100) as executor:
    processes = [executor.submit(checker, token) for token in token_list]
for result in as_completed(processes):
    print(result.result())

print("time taken:")
print(time() - start, "seconds")

def spammer(token):
    headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "content-type": "application/json",
            "authorization": token
    }
    data = {
        "content": "f"
    }
    result = requests.post("https://discord.com/api/v8/channels/834299267308453890/messages", headers=headers, data=data).json()
    return result


start = time()

# with ThreadPoolExecutor(max_workers=100) as executor:
#     processes = [executor.submit(spammer, token) for token in token_list]
# for result in as_completed(processes):
#     print(result.result())

print("time taken:")
print(time() - start, "seconds")