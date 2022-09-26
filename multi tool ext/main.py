# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os
import atexit
import requests
import types
from datetime import datetime

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.settings import Settings

# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from gui.uis.windows.main_window import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# IMPORT APP_FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui.core.app_functions.accounts import Accounts
from gui.core.app_functions.generator import Generator
from gui.widgets.py_popup import PyPopup

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"


# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        Core.log_info("Welcome to Artiko Multi Tool")
        # SETUP MAIN WINDOW
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_LoginWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True  # Show/Hide resize grips
        self.main_window = SetupLoginWindow.setup_gui(self)

        self.line_edit.returnPressed.connect(lambda: self.login_auth(False))

        self.loop = QEventLoop(self)

    def login_auth(self, saved):
        if self.line_edit.text():
            self.change_text("Authenticating...", "white")
            Core.log_info("Authenticating...")
            resp = requests.get("https://mocki.io/v1/958f49a2-6113-4e82-be31-48502341558a")
            if resp.status_code == 200:
                if resp.json().get('status') == 1:
                    self.change_text("Successfully Authenticated", "green")
                    Core.log_info("Successfully Authenticated")
                    if not saved:
                        config = Core.get_config()
                        key = self.line_edit.text()
                        config['key'] = key
                        Core.write_config(config)
                        Core.log_info("Saved Key")
                    QTimer.singleShot(1000, self.accept)
            else:
                self.change_text("Unable to connect to Artiko Authentication", "red")
                Core.log_error("Unable to connect to Artiko Authentication")
                Core.log_error("Please check internet connection")
        else:
            self.change_text("Please enter your key", "red")
            Core.log_error("Key not entered")

    def change_text(self, text, color):
        self.text.setText(text)
        self.text.setStyleSheet(f"color: {color};")
        self.text_time = datetime.now()
        QTimer.singleShot(5001, self.clear_text)

    def clear_text(self):
        if (datetime.now() - self.text_time).total_seconds() >= 5:
            self.text.setText("")
            self.text.setStyleSheet(f"color: white;")

    def accept(self):
        self.loop.exit(True)

    def showEvent(self, event):
        key = Core.get_config().get('key')
        if key:
            self.line_edit.setText(key)
            self.change_text("Key Found", "white")
            Core.log_info("Key Found")
            QTimer.singleShot(200, lambda: self.login_auth(True))

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupLoginWindow.resize_grips(self)
        # self.loop.exit(True)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

    def closeEvent(self, event):
        self.loop.exit(False)

    def exec(self):
        self.show()
        result = self.loop.exec()
        self.hide()
        return result


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        self.popup_list = []
        self.btn_active = ""

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True  # Show/Hide resize grips
        self.main_window = SetupMainWindow.setup_gui(self)
        self.accounts = Accounts(self.ui.load_pages.page_3, self.ui.load_pages.table_layout, self.main_window.footer_text)

        # connect table options buttons
        # ///////////////////////////////////////////////////////////////
        self.options_check.clicked.connect(lambda: self.accounts.options_check(self.right_check_toggle.isChecked()))
        self.options_add.clicked.connect(self.accounts.options_add)
        self.options_export.clicked.connect(lambda: self.accounts.options_export(self.right_export_toggle.isChecked()))
        self.options_edit.clicked.connect(lambda: Core.log_warning("Feature coming soon"))

        self.right_check_toggle.clicked.connect(lambda: self.accounts.toggle_check(self.right_check_toggle.isChecked()))
        self.right_export_toggle.clicked.connect(lambda: self.accounts.toggle_export(self.right_export_toggle.isChecked()))

        # connect table footer option buttons
        # ///////////////////////////////////////////////////////////////
        self.footer_toggle.clicked.connect(self.accounts.toggle_all_accounts)
        self.footer_delete_disabled.clicked.connect(self.accounts.delete_disabled_accounts)
        self.footer_delete_all.clicked.connect(self.accounts.delete_all_accounts)
        self.footer_refresh.clicked.connect(self.accounts.refresh_accounts)

        self.setDefault()

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

        # download chromedriver
        QTimer.singleShot(1000, self.accounts.install_chromedriver)

    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # Remove Selection If Clicked By "btn_close_left_column"
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()

        # Get Title Bar Btn And Reset Active         
        top_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")
        top_settings.set_active(False)

        # table handler
        self.accounts.table_handler(btn.objectName(), self.ui.load_pages.pages.currentIndex())

        # LEFT MENU
        # ///////////////////////////////////////////////////////////////

        # HOME BTN
        if btn.objectName() == "btn_home":
            Generator()

            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.page_1)
            MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

            try:
                self.popup.reject()
            except:
                pass

        # ACCOUNTS BTN
        if btn.objectName() == "btn_accounts":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_3)
            MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_3)

            try:
                self.popup.reject()
            except:
                pass

        # ATTACK BTN
        if btn.objectName() == "btn_attack":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_3)
            MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_3)

            self.popup = PyPopup(self.ui.load_pages.page_3, "editAll")
            self.popup.exec()

        if btn.objectName() == "btn_info":
            if not MainFunctions.left_column_is_visible(self):
                self.ui.left_menu.select_only_one_tab(btn.objectName())
                # Show / Hide
                MainFunctions.toggle_left_column(self)
            else:
                if self.btn_active == "info":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                    self.btn_active = ""
                else:
                    self.ui.left_menu.select_only_one_tab(btn.objectName())
            self.btn_active = "info"
            MainFunctions.set_left_column_menu(
                self,
                menu=self.ui.left_column.menus.menu_2,
                title="Info tab",
                icon_path=Functions.set_svg_icon("icon_info.svg")
            )

        if btn.objectName() == "btn_settings":
            if not MainFunctions.left_column_is_visible(self):
                self.ui.left_menu.select_only_one_tab(btn.objectName())
                # Show / Hide
                MainFunctions.toggle_left_column(self)
            else:
                if self.btn_active == "settings":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                    self.btn_active = ""
                else:
                    self.ui.left_menu.select_only_one_tab(btn.objectName())
            self.btn_active = "settings"
            MainFunctions.set_left_column_menu(
                self,
                menu=self.ui.left_column.menus.menu_1,
                title="Settings tab",
                icon_path=Functions.set_svg_icon("icon_info.svg")
            )

        if btn.objectName() == "btn_close_left_column" and self.btn_active != "":
            self.ui.left_menu.deselect_all_tab()
            # Show / Hide
            MainFunctions.toggle_left_column(self)
            self.btn_active = ""

        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////

        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn            
            top_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            top_settings.set_active_tab(False)

    def setDefault(self):
        config = Core.get_config()
        if config.get('accounts').get('disable toggle'):
            self.right_check_toggle.setChecked(config.get('accounts').get('disable toggle'))
        if config.get('accounts').get('export type'):
            self.right_export_toggle.setChecked(config.get('accounts').get('export type'))

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()


def on_exit():
    Core.log_info("Closing")
    config = Core.get_config()
    config['log_file'] = ""
    Core.write_config(config)


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    atexit.register(on_exit)
    Core.create_config_file()
    app = QApplication()
    app.setWindowIcon(QIcon("icon.ico"))
    login = LoginWindow()
    if login.exec():
        window = MainWindow()
        sys.exit(app.exec())
    else:
        sys.exit()
