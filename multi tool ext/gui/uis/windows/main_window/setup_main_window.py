# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from .functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from .ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from .functions_main_window import *

from gui.uis.windows.main_window import *
from gui.core.functions import Functions
from .ui_main import *


# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupLoginWindow:
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])

        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        themes = Themes()
        self.themes = themes.items

        settings = Settings()
        self.settings = settings.items

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)

        # PY LINE EDIT
        self.line_edit = PyLineEdit(
            text="",
            place_holder_text="License Key",
            alignment=Qt.AlignCenter,
            echo_mode=QLineEdit.Password,
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit.setMinimumHeight(50)

        self.ui.load_pages.key_input_layout.addWidget(self.line_edit)

        self.text = QLabel()
        self.text.setWordWrap(True)
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setStyleSheet("font-size: 11pt;")
        self.ui.load_pages.text_layout.addWidget(self.text)

        self.logo_svg = QSvgWidget(Functions.set_svg_image("artiko logo home.svg"))
        self.ui.load_pages.logo_layout.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)


class SetupMainWindow:
    add_left_menus = [
        {
            "btn_icon": "icon_home.svg",
            "btn_id": "btn_home",
            "btn_text": "Home",
            "btn_tooltip": "Home",
            "show_top": True,
            "is_active": True
        },
        {
            "btn_icon": "icon_add_user.svg",
            "btn_id": "btn_gen",
            "btn_text": "Generator",
            "btn_tooltip": "Generator",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_folder_open.svg",
            "btn_id": "btn_accounts",
            "btn_text": "Accounts",
            "btn_tooltip": "Accounts",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_signal.svg",
            "btn_id": "btn_attack",
            "btn_text": "Attack",
            "btn_tooltip": "Attack",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_info.svg",
            "btn_id": "btn_info",
            "btn_text": "Information",
            "btn_tooltip": "Open informations",
            "show_top": False,
            "is_active": False
        },
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "btn_settings",
            "btn_text": "App Settings",
            "btn_tooltip": "Open settings",
            "show_top": False,
            "is_active": False
        }
    ]

    # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "btn_top_settings",
            "btn_tooltip": "Page Settings",
            "is_active": False
        }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])

        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu=self.ui.left_column.menus.menu_1,
            title="Settings Left Column",
            icon_path=Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # PAGES
        # ///////////////////////////////////////////////////////////////

        # PAGE 1 - ADD LOGO TO MAIN PAGE
        # ///////////////////////////////////////////////////////////////
        self.logo_svg = QSvgWidget(Functions.set_svg_image("artiko logo home.svg"))
        self.ui.load_pages.logo_layout.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)

        # PAGE 3 - Accounts
        # ///////////////////////////////////////////////////////////////
        # options
        self.options_check = PyPushButton(
            text="Check",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_one"],
            bg_color_hover=self.themes["app_color"]["dark_four"],
            bg_color_pressed=self.themes["app_color"]["dark_three"]
        )
        self.options_check.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.ui.load_pages.options_layout.addWidget(self.options_check)

        self.options_add = PyPushButton(
            text="Add",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_one"],
            bg_color_hover=self.themes["app_color"]["dark_four"],
            bg_color_pressed=self.themes["app_color"]["dark_three"]
        )
        self.options_add.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.ui.load_pages.options_layout.addWidget(self.options_add)

        self.options_export = PyPushButton(
            text="Export",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_one"],
            bg_color_hover=self.themes["app_color"]["dark_four"],
            bg_color_pressed=self.themes["app_color"]["dark_three"]
        )
        self.options_export.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.ui.load_pages.options_layout.addWidget(self.options_export)

        self.options_edit = PyPushButton(
            text="Edit",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_one"],
            bg_color_hover=self.themes["app_color"]["dark_four"],
            bg_color_pressed=self.themes["app_color"]["dark_three"]
        )
        self.options_edit.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.ui.load_pages.options_layout.addWidget(self.options_edit)

        self.footer_toggle = PyPushButton(
            text="Toggle All",
            radius=0,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_hover=self.themes["app_color"]["bg_two"],
            bg_color_pressed=self.themes["app_color"]["bg_two"]
        )
        self.footer_toggle.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.footer_toggle.setFixedWidth(100)
        self.ui.load_pages.footer_options_layout.addWidget(self.footer_toggle)

        self.footer_delete_disabled = PyPushButton(
            text="Delete Disabled",
            radius=0,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_hover=self.themes["app_color"]["bg_two"],
            bg_color_pressed=self.themes["app_color"]["bg_two"]
        )
        self.footer_delete_disabled.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.footer_delete_disabled.setFixedWidth(125)
        self.ui.load_pages.footer_options_layout.addWidget(self.footer_delete_disabled)

        self.footer_delete_all = PyPushButton(
            text="Delete All",
            radius=0,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_hover=self.themes["app_color"]["bg_two"],
            bg_color_pressed=self.themes["app_color"]["bg_two"]
        )
        self.footer_delete_all.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.footer_delete_all.setFixedWidth(100)
        self.ui.load_pages.footer_options_layout.addWidget(self.footer_delete_all)

        self.footer_refresh = PyPushButton(
            text="Refresh",
            radius=0,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_two"],
            bg_color_hover=self.themes["app_color"]["bg_two"],
            bg_color_pressed=self.themes["app_color"]["bg_two"]
        )
        self.footer_refresh.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.footer_refresh.setFixedWidth(100)
        self.ui.load_pages.footer_options_layout.addWidget(self.footer_refresh)

        self.ui.load_pages.footer_options_layout.setAlignment(Qt.AlignLeft)
        self.ui.load_pages.footer_options.setStyleSheet("font: 12pt;")

        self.footer_text = QLabel()
        self.footer_text.setStyleSheet("font: 12pt;")

        self.ui.load_pages.footer_text_layout.addWidget(self.footer_text)

        # RIGHT COLUMN
        # ///////////////////////////////////////////////////////////////
        self.right_check_text = QLabel("Disable bad accounts")
        self.right_check_text.setWordWrap(True)
        self.right_check_text.setAlignment(Qt.AlignCenter)
        self.right_check_text.setStyleSheet("font: 15pt")
        self.right_check_toggle = PyToggle(
            width=40,
            height=21,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["icon_color"],
            active_color=self.themes["app_color"]["context_color"]
        )
        self.ui.right_column.check_toggle_layout.addWidget(self.right_check_text, 1, Qt.AlignCenter)
        self.ui.right_column.check_toggle_layout.addWidget(self.right_check_toggle, 1, Qt.AlignCenter)

        self.right_export_text = QLabel("Export Format")
        self.right_export_text.setWordWrap(True)
        self.right_export_text.setAlignment(Qt.AlignCenter)
        self.right_export_text.setStyleSheet("font: 15pt")
        self.right_export_choice = QWidget()
        self.right_export_choice_layout = QHBoxLayout(self.right_export_choice)
        self.right_export_choice_1 = QLabel("token")
        self.right_export_choice_2 = QLabel("email:pass:token")
        self.right_export_toggle = PyToggle(
            width=40,
            height=21,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["icon_color"],
            active_color=self.themes["app_color"]["context_color"]
        )
        self.right_export_choice_layout.addWidget(self.right_export_choice_1)
        self.right_export_choice_layout.addWidget(self.right_export_toggle)
        self.right_export_choice_layout.addWidget(self.right_export_choice_2)
        self.ui.right_column.export_toggle_layout.addWidget(self.right_export_text, 1)
        self.ui.right_column.export_toggle_layout.addWidget(self.right_export_choice, 1, Qt.AlignCenter)

        self.ui.right_column.menu_2_layout.setAlignment(Qt.AlignTop)

        return self

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)
