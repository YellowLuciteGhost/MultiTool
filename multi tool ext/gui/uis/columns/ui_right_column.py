# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *


class Ui_RightColumn(object):
    def setupUi(self, RightColumn):
        if not RightColumn.objectName():
            RightColumn.setObjectName(u"RightColumn")
        RightColumn.resize(240, 600)
        self.horizontalLayout = QHBoxLayout(RightColumn)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(RightColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.menu_1_layout = QVBoxLayout(self.menu_1)
        self.menu_1_layout.setSpacing(5)
        self.menu_1_layout.setObjectName(u"menu_1_layout")
        self.menu_1_layout.setContentsMargins(5, 5, 5, 5)
        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.menu_2_layout = QVBoxLayout(self.menu_2)
        self.menu_2_layout.setSpacing(5)
        self.menu_2_layout.setObjectName(u"menu_2_layout")
        self.menu_2_layout.setContentsMargins(5, 5, 5, 5)
        self.menus.addWidget(self.menu_2)
        self.menu_3 = QWidget()
        self.menu_3.setObjectName(u"menu_3")
        self.menu_3_layout = QVBoxLayout(self.menu_3)
        self.menu_3_layout.setSpacing(5)
        self.menu_3_layout.setObjectName(u"menu_3_layout")
        self.menu_3_layout.setContentsMargins(5, 5, 5, 5)
        self.check_toggle = QFrame(self.menu_3)
        self.check_toggle.setObjectName(u"check_toggle")
        self.check_toggle.setMinimumSize(QSize(0, 100))
        self.check_toggle.setMaximumSize(QSize(16777215, 100))
        self.check_toggle.setFrameShape(QFrame.NoFrame)
        self.check_toggle.setFrameShadow(QFrame.Raised)
        self.check_toggle_layout = QVBoxLayout(self.check_toggle)
        self.check_toggle_layout.setSpacing(0)
        self.check_toggle_layout.setObjectName(u"check_toggle_layout")
        self.check_toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.menu_3_layout.addWidget(self.check_toggle)

        self.export_toggle = QFrame(self.menu_3)
        self.export_toggle.setObjectName(u"export_toggle")
        self.export_toggle.setMinimumSize(QSize(0, 100))
        self.export_toggle.setMaximumSize(QSize(16777215, 100))
        self.export_toggle.setFrameShape(QFrame.NoFrame)
        self.export_toggle.setFrameShadow(QFrame.Raised)
        self.export_toggle_layout = QVBoxLayout(self.export_toggle)
        self.export_toggle_layout.setSpacing(0)
        self.export_toggle_layout.setObjectName(u"export_toggle_layout")
        self.export_toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.menu_3_layout.addWidget(self.export_toggle)

        self.menus.addWidget(self.menu_3)

        self.horizontalLayout.addWidget(self.menus)


        self.retranslateUi(RightColumn)

        self.menus.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(RightColumn)
    # setupUi

    def retranslateUi(self, RightColumn):
        RightColumn.setWindowTitle(QCoreApplication.translate("RightColumn", u"Form", None))
    # retranslateUi
