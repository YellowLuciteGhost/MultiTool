from qt_core import *


class Ui_addAccountPopup(object):
    def setupUi(self, addAccountPopup):
        if not addAccountPopup.objectName():
            addAccountPopup.setObjectName(u"addAccountPopup")
        addAccountPopup.resize(889, 770)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addAccountPopup.sizePolicy().hasHeightForWidth())
        addAccountPopup.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(addAccountPopup)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 20, 0, 20)
        self.main = QFrame(addAccountPopup)
        self.main.setObjectName(u"main")
        self.main.setMinimumSize(QSize(650, 0))
        self.main.setMaximumSize(QSize(650, 16777215))
        self.main.setFrameShape(QFrame.NoFrame)
        self.main.setFrameShadow(QFrame.Raised)
        self.main_layout = QVBoxLayout(self.main)
        self.main_layout.setObjectName(u"main_layout")
        self.scrollArea = QScrollArea(self.main)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 615, 712))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title = QLabel(self.scrollAreaWidgetContents)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 40))
        self.title.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title)

        self.sub_title = QLabel(self.scrollAreaWidgetContents)
        self.sub_title.setObjectName(u"sub_title")
        self.sub_title.setMinimumSize(QSize(0, 40))
        self.sub_title.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(15)
        self.sub_title.setFont(font1)
        self.sub_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.sub_title)

        self.account_input = QFrame(self.scrollAreaWidgetContents)
        self.account_input.setObjectName(u"account_input")
        self.account_input.setFrameShape(QFrame.NoFrame)
        self.account_input.setFrameShadow(QFrame.Raised)
        self.account_input_layout = QVBoxLayout(self.account_input)
        self.account_input_layout.setSpacing(0)
        self.account_input_layout.setObjectName(u"account_input_layout")
        self.account_input_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.account_input)

        self.button = QFrame(self.scrollAreaWidgetContents)
        self.button.setObjectName(u"button")
        self.button.setMinimumSize(QSize(0, 50))
        self.button.setMaximumSize(QSize(16777215, 50))
        self.button.setFrameShape(QFrame.NoFrame)
        self.button.setFrameShadow(QFrame.Raised)
        self.button_layout = QVBoxLayout(self.button)
        self.button_layout.setSpacing(0)
        self.button_layout.setObjectName(u"button_layout")
        self.button_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.button)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.main_layout.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.main, 0, Qt.AlignHCenter)


        self.retranslateUi(addAccountPopup)

        QMetaObject.connectSlotsByName(addAccountPopup)
    # setupUi

    def retranslateUi(self, addAccountPopup):
        addAccountPopup.setWindowTitle(QCoreApplication.translate("addAccountPopup", u"Form", None))
        self.title.setText(QCoreApplication.translate("addAccountPopup", u"Add Accounts", None))
        self.sub_title.setText(QCoreApplication.translate("addAccountPopup", u"\"token\" or \"email:pass:token\"", None))
    # retranslateUi


class Ui_editAllPopup(object):
    def setupUi(self, editAllPopup):
        if not editAllPopup.objectName():
            editAllPopup.setObjectName(u"editAllPopup")
        editAllPopup.resize(889, 770)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(editAllPopup.sizePolicy().hasHeightForWidth())
        editAllPopup.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(editAllPopup)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 20, 0, 20)
        self.main = QFrame(editAllPopup)
        self.main.setObjectName(u"main")
        self.main.setMinimumSize(QSize(650, 0))
        self.main.setMaximumSize(QSize(650, 16777215))
        self.main.setFrameShape(QFrame.NoFrame)
        self.main.setFrameShadow(QFrame.Raised)
        self.main_layout = QVBoxLayout(self.main)
        self.main_layout.setObjectName(u"main_layout")
        self.scrollArea = QScrollArea(self.main)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 615, 720))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title = QLabel(self.scrollAreaWidgetContents)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 40))
        self.title.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title)

        self.table = QFrame(self.scrollAreaWidgetContents)
        self.table.setObjectName(u"table")
        self.table.setMinimumSize(QSize(0, 400))
        self.table.setMaximumSize(QSize(16777215, 400))
        self.table.setFrameShape(QFrame.NoFrame)
        self.table.setFrameShadow(QFrame.Raised)
        self.table_layout = QVBoxLayout(self.table)
        self.table_layout.setSpacing(0)
        self.table_layout.setObjectName(u"table_layout")
        self.table_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.table)

        self.toggle = QFrame(self.scrollAreaWidgetContents)
        self.toggle.setObjectName(u"toggle")
        self.toggle.setMinimumSize(QSize(0, 50))
        self.toggle.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(6)
        self.toggle.setFont(font1)
        self.toggle.setFrameShape(QFrame.NoFrame)
        self.toggle.setFrameShadow(QFrame.Raised)
        self.toggle_layout = QVBoxLayout(self.toggle)
        self.toggle_layout.setSpacing(0)
        self.toggle_layout.setObjectName(u"toggle_layout")
        self.toggle_layout.setContentsMargins(0, 0, 0, 0)
        self.toggle_button = QFrame(self.toggle)
        self.toggle_button.setObjectName(u"toggle_button")
        self.toggle_button.setFrameShape(QFrame.NoFrame)
        self.toggle_button.setFrameShadow(QFrame.Raised)
        self.toggle_button_layout = QVBoxLayout(self.toggle_button)
        self.toggle_button_layout.setSpacing(0)
        self.toggle_button_layout.setObjectName(u"toggle_button_layout")
        self.toggle_button_layout.setContentsMargins(0, 0, 0, 0)

        self.toggle_layout.addWidget(self.toggle_button)

        self.toggle_text = QLabel(self.toggle)
        self.toggle_text.setObjectName(u"toggle_text")
        font2 = QFont()
        font2.setPointSize(11)
        self.toggle_text.setFont(font2)
        self.toggle_text.setAlignment(Qt.AlignCenter)

        self.toggle_layout.addWidget(self.toggle_text)


        self.verticalLayout_2.addWidget(self.toggle)

        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 30))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 30))
        self.lineEdit_4.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.button = QFrame(self.scrollAreaWidgetContents)
        self.button.setObjectName(u"button")
        self.button.setMinimumSize(QSize(0, 50))
        self.button.setMaximumSize(QSize(16777215, 50))
        self.button.setFrameShape(QFrame.NoFrame)
        self.button.setFrameShadow(QFrame.Raised)
        self.button_layout = QVBoxLayout(self.button)
        self.button_layout.setSpacing(0)
        self.button_layout.setObjectName(u"button_layout")
        self.button_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.button)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.main_layout.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.main, 0, Qt.AlignHCenter)


        self.retranslateUi(editAllPopup)

        QMetaObject.connectSlotsByName(editAllPopup)
    # setupUi

    def retranslateUi(self, editAllPopup):
        editAllPopup.setWindowTitle(QCoreApplication.translate("editAllPopup", u"Form", None))
        self.title.setText(QCoreApplication.translate("editAllPopup", u"Edit Accounts", None))
        self.toggle_text.setText(QCoreApplication.translate("editAllPopup", u"X Accounts Selected", None))
    # retranslateUi
