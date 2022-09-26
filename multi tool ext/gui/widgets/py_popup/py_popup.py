from qt_core import *
from gui.uis.windows.popups import *
from gui.core.json_themes import Themes


class PyPopup(QWidget):
    def __init__(self, parent, type):
        super().__init__(parent)

        self.parent = parent

        themes = Themes()
        self.themes = themes.items

        self.setFocus()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setAttribute(Qt.WA_StyledBackground)

        if type == "editAll":
            self.ui = UI_EditAllPopup()
            self.ui.setup_ui(self)
            self.popup_window = SetupEditAllPopup
            self.popup_window.setup_gui(self)
        elif type == "add":
            self.ui = UI_AddAccountPopup()
            self.ui.setup_ui(self)
            self.popup_window = SetupAddAccountPopup
            self.popup_window.setup_gui(self)

        parent.installEventFilter(self)
        self.loop = QEventLoop(self)

    def accept(self):
        self.loop.exit(True)

    def reject(self):
        self.loop.exit(False)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.reject()

    def mouseReleaseEvent(self, event):
        if not self.ui.load_popup.main.underMouse():
            self.reject()

    def showEvent(self, event):
        self.setGeometry(self.parent.rect())
        self.setStyleSheet("border-radius: 8px; background: rgba(0, 0, 0, 0.33);")
        self.ui.load_popup.main.setStyleSheet(f"""
            QWidget {{
                background: {self.themes['app_color']['bg_two']};
                border-radius: 10px;
            }}
            QLabel#title {{
                font: 24pt;
            }}
        """)
        self.ui.load_popup.scrollArea.setStyleSheet(f"""
            QScrollBar:horizontal {{
                border: none;
                background: {self.themes["app_color"]["bg_one"]};
                height: 8px;
                margin: 0px 21px 0 21px;
                border-radius: 0px;
            }}
            QScrollBar::handle:horizontal {{
                background: {self.themes["app_color"]["context_color"]};
                min-width: 25px;
                border-radius: 4px
            }}
            QScrollBar::add-line:horizontal {{
                border: none;
                background: {self.themes["app_color"]["dark_four"]};
                width: 20px;
                border-top-right-radius: 4px;
                border-bottom-right-radius: 4px;
                subcontrol-position: right;
                subcontrol-origin: margin;
            }}
            QScrollBar::sub-line:horizontal {{
                border: none;
                background: {self.themes["app_color"]["dark_four"]};
                width: 20px;
                border-top-left-radius: 4px;
                border-bottom-left-radius: 4px;
                subcontrol-position: left;
                subcontrol-origin: margin;
            }}
            QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {{
                background: none;
            }}
            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {{
                background: none;
            }}
            QScrollBar:vertical {{
                border: none;
                background: {self.themes["app_color"]["bg_one"]};
                width: 8px;
                margin: 21px 0 21px 0;
                border-radius: 0px;
            }}
            QScrollBar::handle:vertical {{
                background: {self.themes["app_color"]["context_color"]};
                min-height: 25px;
                border-radius: 4px
            }}
            QScrollBar::add-line:vertical {{
                border: none;
                background: {self.themes["app_color"]["dark_four"]};
                height: 20px;
                border-bottom-left-radius: 4px;
                border-bottom-right-radius: 4px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }}
            QScrollBar::sub-line:vertical {{
                border: none;
                background: {self.themes["app_color"]["dark_four"]};
                height: 20px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }}
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
                background: none;
            }}
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
                background: none;
            }}
        """)

    def close(self):
        self.loop.quit()

    def exec(self):
        self.show()
        self.raise_()
        res = self.loop.exec()
        self.hide()
        return res
