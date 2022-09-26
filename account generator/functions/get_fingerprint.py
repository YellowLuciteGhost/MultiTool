import selrequests
import chromedriver_autoinstaller


def get_fingerprint():
    chromedriver_autoinstaller.install()
    sel = selrequests.Session()
    sel.set_origin("https://discord.com/")
    with sel.request(method="GET", url="https://discord.com/api/v8/experiments") as resp:
        data = resp.json()
    return data.get("fingerprint")
