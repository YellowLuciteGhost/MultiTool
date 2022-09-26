import re
import datetime
import imap_tools
import requests


def get_verify_link(email, password):
    if re.match(r"^([A-Z|a-z|0-9](\.|_){0,1})+[A-Z|a-z|0-9]\@([A-Z|a-z|0-9])+((\.){0,1}[A-Z|a-z|0-9]){2}\.[a-z]{2,3}$", email):
        with imap_tools.MailBox('imap.mail.ru').login(email, password, initial_folder='INBOX') as mailbox:
            now = datetime.datetime.utcnow().replace(microsecond=0)
            for mail in mailbox.fetch(reverse=True):
                if mail.from_ == 'noreply@discord.com' and mail.subject == 'Verify Email Address for Discord':
                    if now - datetime.timedelta(minutes=60) <= mail.date.replace(tzinfo=None) <= now:
                        click_link = re.search("(?P<url>https?://[^\s]+)", mail.text).group("url")
                        if click_link:
                            resp = requests.get(click_link)
                            verify_link = resp.url
                            return verify_link
            else:
                return False
