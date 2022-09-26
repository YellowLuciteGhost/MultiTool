import os
import json
from datetime import datetime
from colorama import Fore


class Core:
    @staticmethod
    def create_config_file():
        if not os.path.exists("data/config.json"):
            with open("data/config.json", "w+") as f:
                json.dump({}, f, indent=4)

    @staticmethod
    def get_accounts():
        with open("data/accounts.json", 'r') as f:
            accounts = json.load(f)
        return accounts

    @staticmethod
    def write_accounts(accounts: dict):
        with open("data/accounts.json", 'w') as f:
            json.dump(accounts, f, indent=4)

    @staticmethod
    def get_config():
        with open("data/config.json", 'r') as f:
            config = json.load(f)
        return config

    @staticmethod
    def write_config(config: dict):
        with open("data/config.json", 'w') as f:
            json.dump(config, f, indent=4)

    @staticmethod
    def create_log_file():
        log_file = f"data/logs/log-{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
        directory = os.path.dirname(log_file)
        if not os.path.exists(directory):
            os.makedirs(directory)
        config = Core.get_config()
        config['log_file'] = log_file
        Core.write_config(config)
        return log_file

    @classmethod
    def get_log_file(cls):
        log_file = Core.get_config().get('log_file')
        if not log_file:
            log_file = Core.create_log_file()
        return log_file

    @staticmethod
    def log_info(message):
        timestamp = datetime.now().strftime('%H:%M:%S')
        print(f"{Fore.GREEN}[+]|{timestamp}|Info: {message}{Fore.RESET}")
        with open(Core.get_log_file(), 'a') as f:
            f.write(f"[+]|{timestamp}|Info: {message}\n")

    @staticmethod
    def log_warning(message):
        timestamp = datetime.now().strftime('%H:%M:%S')
        print(f"{Fore.YELLOW}[-]|{timestamp}|Warning: {message}{Fore.RESET}")
        with open(Core.get_log_file(), 'a') as f:
            f.write(f"[-]|{timestamp}|Warning: {message}\n")

    @staticmethod
    def log_error(message):
        timestamp = datetime.now().strftime('%H:%M:%S')
        print(f"{Fore.RED}[!]|{timestamp}|Error: {message}{Fore.RESET}")
        with open(Core.get_log_file(), 'a') as f:
            f.write(f"[!]|{timestamp}|Error: {message}\n")
