# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *


class Ui_LoginPages(object):
    def setupUi(self, LoginPages):
        if not LoginPages.objectName():
            LoginPages.setObjectName(u"LoginPages")
        LoginPages.resize(860, 594)
        self.login_pages_layout = QVBoxLayout(LoginPages)
        self.login_pages_layout.setSpacing(0)
        self.login_pages_layout.setObjectName(u"login_pages_layout")
        self.login_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(LoginPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.login_base = QFrame(self.page_1)
        self.login_base.setObjectName(u"login_base")
        self.login_base.setMinimumSize(QSize(300, 260))
        self.login_base.setMaximumSize(QSize(300, 260))
        self.login_base.setFrameShape(QFrame.NoFrame)
        self.login_base.setFrameShadow(QFrame.Raised)
        self.login_base_layout = QVBoxLayout(self.login_base)
        self.login_base_layout.setSpacing(0)
        self.login_base_layout.setObjectName(u"login_base_layout")
        self.login_base_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.login_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 150))
        self.logo.setMaximumSize(QSize(300, 150))
        self.logo.setStyleSheet(u"font-size: 14pt")
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.login_base_layout.addWidget(self.logo)

        self.key_input = QFrame(self.login_base)
        self.key_input.setObjectName(u"key_input")
        self.key_input.setMinimumSize(QSize(300, 50))
        self.key_input.setMaximumSize(QSize(300, 50))
        self.key_input.setFrameShape(QFrame.NoFrame)
        self.key_input.setFrameShadow(QFrame.Raised)
        self.key_input_layout = QVBoxLayout(self.key_input)
        self.key_input_layout.setSpacing(0)
        self.key_input_layout.setObjectName(u"key_input_layout")
        self.key_input_layout.setContentsMargins(0, 0, 0, 0)

        self.login_base_layout.addWidget(self.key_input)

        self.text = QFrame(self.login_base)
        self.text.setObjectName(u"text")
        self.text.setMinimumSize(QSize(300, 60))
        self.text.setMaximumSize(QSize(300, 60))
        self.text.setFrameShape(QFrame.NoFrame)
        self.text.setFrameShadow(QFrame.Raised)
        self.text_layout = QVBoxLayout(self.text)
        self.text_layout.setSpacing(0)
        self.text_layout.setObjectName(u"text_layout")
        self.text_layout.setContentsMargins(0, 10, 0, 0)

        self.login_base_layout.addWidget(self.text)


        self.page_1_layout.addWidget(self.login_base, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pages.addWidget(self.page_1)

        self.login_pages_layout.addWidget(self.pages)


        self.retranslateUi(LoginPages)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LoginPages)
    # setupUi

    def retranslateUi(self, LoginPages):
        LoginPages.setWindowTitle(QCoreApplication.translate("LoginPages", u"Form", None))
    # retranslateUi


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 594)
        self.verticalLayout_3 = QVBoxLayout(MainPages)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_1)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 200))
        self.welcome_base.setMaximumSize(QSize(300, 200))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.welcome_base)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.artiko_logo = QFrame(self.welcome_base)
        self.artiko_logo.setObjectName(u"artiko_logo")
        self.artiko_logo.setMinimumSize(QSize(300, 150))
        self.artiko_logo.setMaximumSize(QSize(300, 150))
        self.artiko_logo.setStyleSheet(u"font-size: 14pt")
        self.artiko_logo.setFrameShape(QFrame.NoFrame)
        self.artiko_logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.artiko_logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.artiko_logo)

        self.welcome_text = QLabel(self.welcome_base)
        self.welcome_text.setObjectName(u"welcome_text")
        self.welcome_text.setMinimumSize(QSize(300, 50))
        self.welcome_text.setMaximumSize(QSize(300, 50))
        font = QFont()
        font.setPointSize(30)
        self.welcome_text.setFont(font)
        self.welcome_text.setStyleSheet(u"font-size: 30pt")
        self.welcome_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.welcome_text)


        self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setSpacing(5)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.page_3_layout.setContentsMargins(5, 5, 5, 5)
        self.options = QFrame(self.page_3)
        self.options.setObjectName(u"options")
        self.options.setMinimumSize(QSize(0, 50))
        self.options.setMaximumSize(QSize(16777215, 50))
        self.options.setFrameShape(QFrame.NoFrame)
        self.options.setFrameShadow(QFrame.Raised)
        self.options_layout = QHBoxLayout(self.options)
        self.options_layout.setSpacing(5)
        self.options_layout.setObjectName(u"options_layout")
        self.options_layout.setContentsMargins(5, 5, 5, 5)

        self.page_3_layout.addWidget(self.options)

        self.table_base = QFrame(self.page_3)
        self.table_base.setObjectName(u"table_base")
        self.table_base.setMaximumSize(QSize(16777215, 16777215))
        self.table_base.setFrameShape(QFrame.NoFrame)
        self.table_base.setFrameShadow(QFrame.Raised)
        self.table_base_layout = QVBoxLayout(self.table_base)
        self.table_base_layout.setSpacing(0)
        self.table_base_layout.setObjectName(u"table_base_layout")
        self.table_base_layout.setContentsMargins(0, 0, 0, 0)
        self.table = QFrame(self.table_base)
        self.table.setObjectName(u"table")
        self.table.setMaximumSize(QSize(16777215, 16777215))
        self.table.setFrameShape(QFrame.NoFrame)
        self.table.setFrameShadow(QFrame.Raised)
        self.table_layout = QVBoxLayout(self.table)
        self.table_layout.setSpacing(0)
        self.table_layout.setObjectName(u"table_layout")
        self.table_layout.setContentsMargins(0, 0, 0, 0)

        self.table_base_layout.addWidget(self.table)

        self.footer = QFrame(self.table_base)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 75))
        self.footer.setMaximumSize(QSize(16777215, 75))
        self.footer.setFrameShape(QFrame.NoFrame)
        self.footer.setFrameShadow(QFrame.Raised)
        self.footer_layout = QVBoxLayout(self.footer)
        self.footer_layout.setSpacing(0)
        self.footer_layout.setObjectName(u"footer_layout")
        self.footer_layout.setContentsMargins(0, 0, 0, 0)
        self.footer_options = QFrame(self.footer)
        self.footer_options.setObjectName(u"footer_options")
        self.footer_options.setFrameShape(QFrame.NoFrame)
        self.footer_options.setFrameShadow(QFrame.Raised)
        self.footer_options_layout = QHBoxLayout(self.footer_options)
        self.footer_options_layout.setSpacing(5)
        self.footer_options_layout.setObjectName(u"footer_options_layout")
        self.footer_options_layout.setContentsMargins(5, 0, 5, 0)

        self.footer_layout.addWidget(self.footer_options)

        self.footer_text = QFrame(self.footer)
        self.footer_text.setObjectName(u"footer_text")
        self.footer_text.setFrameShape(QFrame.NoFrame)
        self.footer_text.setFrameShadow(QFrame.Raised)
        self.footer_text_layout = QHBoxLayout(self.footer_text)
        self.footer_text_layout.setSpacing(0)
        self.footer_text_layout.setObjectName(u"footer_text_layout")
        self.footer_text_layout.setContentsMargins(25, 0, 0, 0)

        self.footer_layout.addWidget(self.footer_text)


        self.table_base_layout.addWidget(self.footer)


        self.page_3_layout.addWidget(self.table_base)

        self.pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet(u"QFrame {\n"
"                                font-size: 16pt;\n"
"                                }\n"
"                            ")
        self.page_4_layout = QVBoxLayout(self.page_4)
        self.page_4_layout.setObjectName(u"page_4_layout")
        self.pages.addWidget(self.page_4)

        self.verticalLayout_3.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.welcome_text.setText(QCoreApplication.translate("MainPages", u"Multi Tool", None))
    # retranslateUi
