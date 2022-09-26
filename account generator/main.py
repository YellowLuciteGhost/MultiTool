import random
import requests
import base64
import json
from functions import *


emails = get_emails()
email = random.choice(emails)
split_email = email.split(':')
print(split_email)
if len(split_email) != 2 or '' in split_email:
    print(f"{email} is invalid")
else:
    user_data = {
        "os": "Windows",
        "browser": "Chrome",
        "device": "",
        "system_locale": "en_US",
        "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "browser_version": "91.0.4472.124",
        "os_version": "10",
        "referrer": "",
        "referring_domain": "",
        "referrer_current": "",
        "referring_domain_current": "",
        "release_channel": "stable",
        "client_build_number": 90176,
        "client_event_source": None
    }
    super_properties = base64.b64encode(bytes(json.dumps(user_data), 'utf-8'))
    fingerprint = get_fingerprint()
    data = {
        "fingerprint": fingerprint,
        "email": split_email[0],
        "username": "im not gay",
        "password": "testpassword1234",
        "invite": None,
        "consent": True,
        "date_of_birth": "1995-12-12",
        "gift_code_sku_id": None,
        "captcha_key": ""
    }
    headers = {
        "accept-language": "en-US",
        "content-length": str(len(str(data))),
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://discord.com",
        "referer": "https://discord.com/register",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "cookie": "",
        "x-fingerprint": fingerprint,
        "x-super-properties": str(super_properties)
    }
    resp = requests.post('https://discord.com/api/v8/auth/register', data=json.dumps(data), headers=headers)
    print(resp.status_code)
    print(resp.json())
    if resp.json()['captcha_key'][0] == "captcha-required":
        data['captcha_key'] = get_captcha_token("capmonster", "1d175d35a9ca134e82b3d631eda542b6")
        resp = requests.post('https://discord.com/api/v8/auth/register', data=json.dumps(data), headers=headers)
        print(resp.status_code)
        print(resp.json())
    verify_link = get_verify_link(split_email[0], split_email[1])
    print(verify_link)
        
# content = get_verify_link(emails[0][0], emails[0][1])
# print(content)
