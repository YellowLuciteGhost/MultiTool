import requests
import random
import base64
import json
import threading
import time
import selrequests
import random
from qt_core import *
from gui.core.json_themes import Themes

class Generator:
    def __init__(self):
        # themes
        themes = Themes()
        self.themes = themes.items

        # user agents
        with open('gui/core/app_functions/user agents.txt', 'r') as f:
            self.user_agents = [ua.strip() for ua in f.readlines()]

        thread = reigsterWorker("email@example.com", "usernameexample", "testpassword", self.user_agents)
        thread.start()


class reigsterWorker(threading.Thread):
    def __init__(self, email, username, password, user_agents):
        super().__init__()
        self.email = email
        self.username = username
        self.password = password
        self.user_agents = user_agents

    def get_user_agent(self):
        ua = random.choice(self.user_agents)
        return ua

    def get_super_properties(self):
        ua = self.get_user_agent()
        user_data = {
            "os": "Windows",
            "browser": "Chrome",
            "device": "",
            "system_locale": "en_US",
            "browser_user_agent": ua,
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
        return super_properties

    def get_fingerprint(self):
        sel = selrequests.Session()
        sel.set_origin("https://discord.com/")
        with sel.request(method="GET", url="https://discord.com/api/v8/experiments") as resp:
            data = resp.json()
        return data.get("fingerprint")

    def get_data(self, fingerprint):
        data = {
            "fingerprint": fingerprint,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "invite": None,
            "consent": True,
            "date_of_birth": "1995-12-12",
            "gift_code_sku_id": None,
            "captcha_key": ""
        }
        return data

    def get_headers(self, data, fingerprint):
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
            "x-super-properties": self.get_super_properties()
        }
        return headers

    def get_captcha_token(self, api_method, api_key):
        url = "https://discord.com/register"
        site_key = "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"

        # capmonster
        if api_method == 'capmonster':
            post_data = {
                "clientKey": api_key,
                "task": {
                    "type": "HCaptchaTaskProxyless",
                    "websiteURL": url,
                    "websiteKey": site_key
                }
            }
            resp = requests.post("https://api.capmonster.cloud/createTask", json=post_data).json()
            captcha_id = resp.get('taskId')
            if not captcha_id:
                return False
            get_data = {
                "clientKey": api_key,
                "taskId": captcha_id
            }
            retries = 0
            while retries <= 60:
                resp = requests.get("https://api.capmonster.cloud/getTaskResult", json=get_data)
                if resp.status_code == 200:
                    if resp.json().get('status') == 'processing':
                        retries += 1
                        time.sleep(2)
                    else:
                        break
                else:
                    break
            captcha_token = resp.json().get('solution').get('gRecaptchaResponse')
            if captcha_token:
                return captcha_token
            else:
                return False

    def run(self):
        fingerprint = self.get_fingerprint()
        data = self.get_data(fingerprint)
        headers = self.get_headers(data, fingerprint)
        resp = requests.post('https://discord.com/api/v8/auth/register', data=json.dumps(data), headers=headers)
        print(resp.status_code)
        print(resp.json())
        if resp.json().get('captcha_key'):
            captcha_key = self.get_captcha_token("capmonster", "1d175d35a9ca134e82b3d631eda542b6")
            data['captcha_key'] = captcha_key
            resp = requests.post('https://discord.com/api/v8/auth/register', data=json.dumps(data), headers=headers)
            print(resp.status_code)
            print(resp.json())
        else:
            print("failed")
            print(resp.json())
