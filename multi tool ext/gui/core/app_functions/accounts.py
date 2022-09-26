import threading
import timeago
import pyperclip
import requests
import string
import random
from qt_core import *
from datetime import datetime
from time import time
from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor, as_completed
from gui.widgets import PyTableWidget, PyToggle, PyIconButton
from gui.core.functions import Functions
from gui.core.json_themes import Themes
from gui.widgets.py_popup import PyPopup
import chromedriver_autoinstaller

class Accounts:
    def __init__(self, parent: QWidget, table_layout: QVBoxLayout, account_count: QLabel):
        themes = Themes()
        self.themes = themes.items
        self.parent = parent
        self.table_layout = table_layout
        self.account_count = account_count

    def install_chromedriver(self):
        Core.log_info("Updating Chromedriver")
        chromedriver_autoinstaller.install()
        Core.log_info("Finished updating Chromedriver")

    def toggle_check(self, checked):
        config = Core.get_config()
        if not config.get('accounts'):
            config['accounts'] = {}
        if checked:
            config['accounts']['disable toggle'] = True
        else:
            config['accounts']['disable toggle'] = False
        Core.write_config(config)

    def toggle_export(self, checked):
        config = Core.get_config()
        if not config.get('accounts'):
            config['accounts'] = {}
        if checked:
            config['accounts']['export type'] = True
        else:
            config['accounts']['export type'] = False
        Core.write_config(config)

    def options_check(self, checked):
        def checker(token):
            headers = {
                "content-type": "application/json",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50",
                "authorization": token
            }
            result = requests.get("https://discordapp.com/api/v8/users/@me/guilds", headers=headers)
            return token, result.status_code
        accounts = Core.get_accounts()
        start = time()
        with ThreadPoolExecutor(max_workers=len(accounts)) as executor:
            processes = [executor.submit(checker, token) for token in accounts if token]
        status_count = [task.result()[1] for task in as_completed(processes)]
        bad_tokens = [task.result()[0] for task in as_completed(processes) if task.result()[1] == 403 or 401]
        verified = status_count.count(200)
        unverified = status_count.count(403)
        invalid = status_count.count(401)
        Core.log_info(f"Finished checking {len(accounts)} tokens in {round(time() - start, 1)} seconds")
        if verified:
            Core.log_info(f"{verified} working tokens")
        if unverified:
            Core.log_warning(f"{unverified} tokens require verification")
        if invalid:
            Core.log_warning(f"{invalid} invalid tokens")
        if checked and bad_tokens:
            for token in bad_tokens:
                accounts[token]['status'] = False
            Core.write_accounts(accounts)
            Core.log_info(f"Disabled {unverified + invalid} bad tokens")
            self.refresh_accounts()

    def options_add(self):
        self.popup = PyPopup(self.parent, "add")
        if self.popup.exec():
            accounts = Core.get_accounts()
            accounts_list = list(accounts)
            count = 0
            for account in self.popup.account_input_box.toPlainText().splitlines():
                account_split = account.split(':')
                if len(account_split) == 1:
                    if (len(account_split[0]) == 59) or (len(account_split[0]) == 88):
                        if account_split[0] not in accounts_list:
                            accounts[account_split[0]] = {'status': True, 'date-added': int(datetime.now().strftime("%Y%m%d%H%M%S")), 'email': '', 'password': ''}
                            count += 1
                        else:
                            Core.log_warning(f"Account already found - {account}")
                    else:
                        Core.log_warning(f"Invalid token input - {account}")
                elif len(account_split) == 3:
                    if ('@' in account_split[0]) and ('.' in account_split[0]):
                        if (len(account_split[2]) == 59) or (len(account_split[2]) == 88):
                            if account_split[2] not in accounts_list:
                                accounts[account_split[2]] = {'status': True, 'date-added': int(datetime.now().strftime("%Y%m%d%H%M%S")), 'email': account_split[0], 'password': account_split[1]}
                                count += 1
                            else:
                                Core.log_warning(f"Account already found - {account}")
                        else:
                            Core.log_warning(f"Invalid token input - {account}")
                    else:
                        Core.log_warning(f"Invalid email input - {account}")
                else:
                    Core.log_warning(f"Invalid input - {account}")
            if count > 0:
                Core.write_accounts(accounts)
                Core.log_info(f"Added {count} new accounts")
                self.refresh_accounts()
            else:
                Core.log_info("No accounts added")

    def options_export(self, checked):
        accounts = Core.get_accounts()
        if accounts:
            export = ""
            for account in accounts:
                if checked:
                    if accounts.get(account).get('email'):
                        export += f"{accounts.get(account).get('email')}:"
                    else:
                        export += f"{''.join(random.choice(string.ascii_letters) for x in range(10)) + '@random.com'}:"
                    if accounts.get(account).get('password'):
                        export += f"{accounts.get(account).get('password')}:"
                    else:
                        export += f"{'random-' + ''.join(random.choice(string.ascii_letters + string.digits) for x in range(5))}:"
                export += f"{account}\n"
            export = export.rstrip()
            export_file, _ = QFileDialog.getSaveFileName(None, "Account Export", "", "Text Files (*.txt)")
            try:
                with open(export_file, 'w') as f:
                    f.write(export)
                Core.log_info(f"Exported {len(accounts)} accounts to {export_file}")
            except FileNotFoundError:
                pass
        else:
            Core.log_warning("No accounts to export")

    def table_handler(self, button, page):
        if button in ["btn_home", "btn_accounts", "btn_attack"]:
            if button == "btn_accounts" and page != 1:
                self.create_table()
            elif button != "btn_accounts":
                self.delete_table()

    def create_table(self):
        # TABLE
        self.table = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_two"],
            bottom_line_color=self.themes["app_color"]["bg_one"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.table.setColumnCount(7)
        self.table.verticalHeader().setDefaultSectionSize(40)
        self.table.setWordWrap(False)
        self.table.setShowGrid(False)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table.setSelectionMode(QAbstractItemView.NoSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText("Token")

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText("Copy")

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText("Status")

        self.column_4 = QTableWidgetItem()
        self.column_4.setTextAlignment(Qt.AlignCenter)
        self.column_4.setText("Date Added")

        self.column_5 = QTableWidgetItem()
        self.column_5.setTextAlignment(Qt.AlignCenter)
        self.column_5.setText("Login")

        self.column_6 = QTableWidgetItem()
        self.column_6.setTextAlignment(Qt.AlignCenter)
        self.column_6.setText("Edit")

        self.column_7 = QTableWidgetItem()
        self.column_7.setTextAlignment(Qt.AlignCenter)
        self.column_7.setText("Delete")

        self.table.setHorizontalHeaderItem(0, self.column_1)
        self.table.setHorizontalHeaderItem(1, self.column_2)
        self.table.setHorizontalHeaderItem(2, self.column_3)
        self.table.setHorizontalHeaderItem(3, self.column_4)
        self.table.setHorizontalHeaderItem(4, self.column_5)
        self.table.setHorizontalHeaderItem(5, self.column_6)
        self.table.setHorizontalHeaderItem(6, self.column_7)
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 50)
        self.table.setColumnWidth(2, 60)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(6, QHeaderView.Stretch)

        self.table_layout.addWidget(self.table)

        self.refresh_accounts()

    def delete_table(self):
        try:
            self.table_layout.removeWidget(self.table)
            self.table.deleteLater()
            self.table = None
        except AttributeError:
            pass

    def refresh_accounts(self, hide_text=None):
        accounts = Core.get_accounts()
        self.table.setRowCount(0)
        if len(accounts):
            Core.log_info(f"Loading {len(accounts)} accounts")
            self.table.hide()
            self.table.setSortingEnabled(False)
            start = time()
            for _ in range(len(accounts)):
                row = self.table.rowCount()
                self.table.insertRow(row)
            for row, token in enumerate(accounts):
                account = accounts[token]
                self.add_account(
                    row,
                    token,
                    account['status'],
                    timeago.format(datetime.strptime(str(account['date-added']), "%Y%m%d%H%M%S"), datetime.now()),
                    account['email'],
                    account['password']
                )
            Core.log_info(f"Loaded {len(accounts)} accounts in {round(time() - start, 2)} seconds")
            self.table.setSortingEnabled(True)
            self.table.show()
        else:
            if not hide_text:
                Core.log_warning("No accounts found")
        self.refresh_accounts_count()

    def refresh_accounts_count(self):
        accounts = Core.get_accounts()
        count = 0
        for account in accounts:
            if accounts.get(account).get('status'):
                count += 1
        self.account_count.setText(f'Total: {len(accounts)} accounts ({count} active)')

    def add_account(self, row, token, status, dateAdded, email, password):
        token_item = QTableWidgetItem(token)
        token_item.setTextAlignment(Qt.AlignVCenter)
        copy_widget = QWidget()
        copy_layout = QVBoxLayout(copy_widget)
        copy_layout.setContentsMargins(0, 0, 0, 0)
        copy_layout.setAlignment(Qt.AlignCenter)
        copy_item = PyIconButton(
            icon_path=Functions.set_svg_icon('icon_copy.svg'),
            width=30,
            height=30,
            radius=8,
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_hover=self.themes["app_color"]["bg_three"],
            bg_color_pressed=self.themes["app_color"]["dark_one"],
        )
        copy_item.clicked.connect(lambda: pyperclip.copy(token))
        copy_layout.addWidget(copy_item)
        toggle_widget = QWidget()
        toggle_layout = QVBoxLayout(toggle_widget)
        toggle_layout.setContentsMargins(0, 0, 0, 0)
        toggle_layout.setAlignment(Qt.AlignCenter)
        toggle_item = PyToggle(
            width=40,
            height=21,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["icon_color"],
            active_color=self.themes["app_color"]["context_color"]
        )
        toggle_item.clicked.connect(lambda: self.toggle_account(toggle_item.isChecked(), token))
        toggle_item.setChecked(status)
        toggle_layout.addWidget(toggle_item)
        date_added_item = QTableWidgetItem(dateAdded)
        date_added_item.setTextAlignment(Qt.AlignCenter)
        login_widget = QWidget()
        login_layout = QVBoxLayout(login_widget)
        login_layout.setContentsMargins(0, 0, 0, 0)
        login_layout.setAlignment(Qt.AlignCenter)
        login_item = PyIconButton(
            icon_path=Functions.set_svg_icon('icon_login.svg'),
            width=30,
            height=30,
            radius=8,
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_hover=self.themes["app_color"]["bg_three"],
            bg_color_pressed=self.themes["app_color"]["dark_one"],
        )
        login_item.clicked.connect(lambda: self.login_button_clicked(token))
        login_layout.addWidget(login_item)
        edit_widget = QWidget()
        edit_layout = QVBoxLayout(edit_widget)
        edit_layout.setContentsMargins(0, 0, 0, 0)
        edit_layout.setAlignment(Qt.AlignCenter)
        edit_item = PyIconButton(
            icon_path=Functions.set_svg_icon('icon_edit.svg'),
            width=30,
            height=30,
            radius=8,
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_hover=self.themes["app_color"]["bg_three"],
            bg_color_pressed=self.themes["app_color"]["dark_one"],
        )
        edit_item.clicked.connect(lambda: self.edit_account(token))
        edit_layout.addWidget(edit_item)
        delete_widget = QWidget()
        delete_layout = QVBoxLayout(delete_widget)
        delete_layout.setContentsMargins(0, 0, 0, 0)
        delete_layout.setAlignment(Qt.AlignCenter)
        delete_item = PyIconButton(
            icon_path=Functions.set_svg_icon('icon_close.svg'),
            width=30,
            height=30,
            radius=8,
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_hover=self.themes["app_color"]["bg_three"],
            bg_color_pressed=self.themes["app_color"]["dark_one"],
        )
        delete_item.clicked.connect(lambda: self.delete_account(token_item, token))
        delete_layout.addWidget(delete_item)
        self.table.setItem(row, 0, token_item)
        self.table.setCellWidget(row, 1, copy_widget)
        self.table.setCellWidget(row, 2, toggle_widget)
        self.table.setItem(row, 3, date_added_item)
        self.table.setCellWidget(row, 4, login_widget)
        self.table.setCellWidget(row, 5, edit_widget)
        self.table.setCellWidget(row, 6, delete_widget)

    def toggle_all_accounts(self):
        accounts = Core.get_accounts()
        if len(accounts):
            if list(accounts.values())[0].get('status'):
                for account in accounts:
                    accounts[account]['status'] = False
            else:
                for account in accounts:
                    accounts[account]['status'] = True
            Core.write_accounts(accounts)
            self.refresh_accounts()
        else:
            Core.log_warning("No accounts found")

    def delete_disabled_accounts(self):
        accounts = Core.get_accounts()
        new_accounts = {}
        deleted = 0
        for account in accounts:
            if accounts.get(account).get('status'):
                new_accounts[account] = accounts[account]
            else:
                deleted += 1
        Core.log_info(f"Deleted {deleted} accounts")
        Core.write_accounts(new_accounts)
        self.refresh_accounts()

    def delete_all_accounts(self):
        Core.write_accounts({})
        self.refresh_accounts(True)
        Core.log_info("All accounts deleted")

    def toggle_account(self, status, token):
        accounts = Core.get_accounts()
        if status:
            accounts[token]['status'] = True
        else:
            accounts[token]['status'] = False
        Core.write_accounts(accounts)
        self.refresh_accounts_count()

    def login_button_clicked(self, token):
        threading.Thread(target=self.log_into_token, args=(token,)).start()

    def log_into_token(self, token):
        driver = webdriver.Chrome()
        driver.get("https://discord.com/login")
        script = 'let token= "' + token + '";function login(e){setInterval(()=>{document.body.appendChild(document.createElement`iframe`).contentWindow.localStorage.token=`"${e}"`},50),setTimeout(()=>{location.reload()}, 500)}login(token);'
        driver.execute_script(script)

    def edit_account(self, token):
        Core.log_warning("Feature coming soon")
        # self.popup = PyPopup(self.parent, "editSingle")
        # self.popup.exec()

    def delete_account(self, token_item, token):
        accounts = Core.get_accounts()
        try:
            del accounts[token]
        except KeyError:
            self.refresh_accounts()
        Core.write_accounts(accounts)
        self.table.removeRow(token_item.row())
