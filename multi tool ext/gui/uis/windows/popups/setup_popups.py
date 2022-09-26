# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
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
from .ui_popups import *

from gui.uis.windows.popups import *
from gui.core.functions import Functions
from .ui_popups import *


# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupAddAccountPopup:
    def setup_gui(self):
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        self.account_input_box = PyPlainTextEdit(
            text="",
            place_holder_text="Paste accounts here",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.ui.load_popup.account_input_layout.addWidget(self.account_input_box)

        self.add_button = PyPushButton(
            text="Add",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["bg_one"],
            bg_color_hover=self.themes["app_color"]["dark_four"],
            bg_color_pressed=self.themes["app_color"]["dark_three"],
            font=15
        )
        self.add_button.setFixedWidth(200)
        self.add_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.add_button.clicked.connect(self.accept)

        self.ui.load_popup.button_layout.addWidget(self.add_button)
        self.ui.load_popup.button_layout.setAlignment(Qt.AlignHCenter)


class SetupEditAllPopup:
    def setup_gui(self):
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        self.selected_account_table = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_one"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_two"],
            bottom_line_color=self.themes["app_color"]["bg_one"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.selected_account_table.setColumnCount(2)
        self.selected_account_table.verticalHeader().setDefaultSectionSize(40)
        self.selected_account_table.setWordWrap(False)
        self.selected_account_table.setShowGrid(False)
        self.selected_account_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.selected_account_table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.selected_account_table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.selected_account_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.selected_account_table.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText("Token")

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText("Selected")

        self.selected_account_table.setHorizontalHeaderItem(0, self.column_1)
        self.selected_account_table.setHorizontalHeaderItem(1, self.column_2)
        self.selected_account_table.setColumnWidth(0, 437)
        self.selected_account_table.setColumnWidth(1, 159)

        self.ui.load_popup.table_layout.addWidget(self.selected_account_table)
