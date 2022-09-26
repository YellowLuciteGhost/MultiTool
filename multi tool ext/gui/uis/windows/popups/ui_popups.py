# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.core.functions import Functions

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

# IMPORT SETUP MAIN WINDOW
# ///////////////////////////////////////////////////////////////
from .setup_popups import *

# IMPORT MAIN WINDOW PAGES / AND SIDE BOXES FOR APP
# ///////////////////////////////////////////////////////////////
from gui.uis.pages.ui_popups_pages import Ui_editAllPopup, Ui_addAccountPopup


class UI_AddAccountPopup(object):
    def setup_ui(self, parent: QWidget):
        if not parent.objectName():
            parent.setObjectName("AddAccountPopup")
        self.parent = parent

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        self.load_popup = Ui_addAccountPopup()
        self.load_popup.setupUi(self.parent)


class UI_EditAllPopup(object):
    def setup_ui(self, parent: QWidget):
        if not parent.objectName():
            parent.setObjectName("EditAllPopup")
        self.parent = parent

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        self.load_popup = Ui_editAllPopup()
        self.load_popup.setupUi(self.parent)
