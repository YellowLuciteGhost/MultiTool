# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui.widgets import PyTableWidget
from qt_core import *
from gui.widgets import PyToggle, PyIconButton
from gui.core.functions import Functions
from gui.core.json_themes import Themes

import pyperclip
from collections import deque
from functools import cached_property

# IMPORT STYLE
# ///////////////////////////////////////////////////////////////
from .style import *


class PyTableWidgetChunk(PyTableWidget):
    started = Signal()
    finished = Signal()

    CHUNK = 50
    INTERVAL = 0

    themes = Themes().items

    def __init__(
            self,
            radius=8,
            color="#FFF",
            bg_color="#444",
            selection_color="#FFF",
            header_horizontal_color="#333",
            header_vertical_color="#444",
            bottom_line_color="#555",
            grid_line_color="#555",
            scroll_bar_bg_color="#FFF",
            scroll_bar_btn_color="#3333",
            context_color="#00ABE8"
    ):
        super().__init__()

        # PARAMETERS

        # SET STYLESHEET
        self.set_stylesheet(
            radius,
            color,
            bg_color,
            header_horizontal_color,
            header_vertical_color,
            selection_color,
            bottom_line_color,
            grid_line_color,
            scroll_bar_bg_color,
            scroll_bar_btn_color,
            context_color
        )

        self.timer.timeout.connect(self.handle_timeout)

    @cached_property
    def queue(self):
        return deque()

    @cached_property
    def timer(self):
        timer = QTimer()
        timer.setInterval(self.INTERVAL)
        return timer

    def fillData(self, data):
        self.started.emit()
        self.queue.clear()
        self.queue.extend(data)
        self.timer.start()

    def handle_timeout(self):
        for i in range(self.CHUNK):
            print(self.queue)
            if self.queue:
                value = self.queue.pop(0)
                print(value)
                self.create_item(value[0], value[1], value[2], value[3], value[4])
            else:
                self.timer.stop()
                self.finished.emit()
                break

    def create_item(self, token, status, dateAdded, email, password):
        row = self.rowCount()
        self.insertRow(row)
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
        self.setItem(row, 0, token_item)
        self.setCellWidget(row, 1, copy_widget)
        self.setCellWidget(row, 2, toggle_widget)
        self.setItem(row, 3, date_added_item)
        self.setCellWidget(row, 4, login_widget)
        self.setCellWidget(row, 5, edit_widget)
        self.setCellWidget(row, 6, delete_widget)
