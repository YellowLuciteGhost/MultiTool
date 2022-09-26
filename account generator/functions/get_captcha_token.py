import hcaptcha_bypass
import requests
import time


def get_captcha_token(captcha_method, api_key):
    url = "https://discord.com/register"
    site_key = "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"

    # capmonster method
    if captcha_method == 'capmonster':
        post = {
            "clientKey": api_key,
            "task": {
                "type": "HCaptchaTaskProxyless",
                "websiteURL": url,
                "websiteKey": site_key
            }
        }
        resp = requests.post("https://api.capmonster.cloud/createTask", json=post).json()
        captcha_id = resp.get('taskId')
        if not captcha_id:
            return False
        get = {
            "clientKey": api_key,
            "taskId": captcha_id
        }
        retries = 0
        while True:
            resp = requests.get("https://api.capmonster.cloud/getTaskResult", json=get).json()
            if resp.get('status') == 'processing':
                if retries >= 60:
                    return False
                retries += 1
                time.sleep(2)
            else:
                break
        captcha_token = resp.get('solution').get('gRecaptchaResponse')
        if captcha_token:
            print(captcha_token)
            return captcha_token
        else:
            return False

    # 2captcha method
    elif captcha_method == '2captcha':
        post = {
            "key": api_key,
            "method": "hcaptcha",
            "sitekey": site_key,
            "pageurl": url,
            "json": 1
        }
        resp = requests.post("http://2captcha.com/in.php", params=post).json()
        captcha_id = resp.get('request')
        if not captcha_id:
            return False
        get = {
            "key": api_key,
            "action": "get",
            "id": captcha_id,
            "json": 1
        }
        retries = 0
        while True:
            resp = requests.get("http://2captcha.com/res.php", params=get).json()
            if resp.get('status') == 0:
                if retries >= 60:
                    return False
                retries += 1
                time.sleep(2)
            else:
                break
        captcha_token = resp.get('request')
        if captcha_token:
            return captcha_token
        else:
            return False
