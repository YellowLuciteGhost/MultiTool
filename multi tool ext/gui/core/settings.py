# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os

# SETTINGS
# ///////////////////////////////////////////////////////////////
settings = {
    "app_name": "Artiko.blue - Multi Tool",
    "version": "v0.0.1",
    "copyright": "Artiko.blue",
    "year": 2021,
    "theme_name": "default",
    "custom_title_bar": True,
    "login_startup_size": [
        400,
        500
    ],
    "login_minimum_size": [
        400,
        500
    ],
    "startup_size": [
        1200,
        720
    ],
    "minimum_size": [
        960,
        540
    ],
    "lef_menu_size": {
        "minimum": 50,
        "maximum": 240
    },
    "left_menu_content_margins": 3,
    "left_column_size": {
        "minimum": 0,
        "maximum": 240
    },
    "right_column_size": {
        "minimum": 0,
        "maximum": 240
    },
    "time_animation": 500,
    "font": {
        "family": "Segoe UI",
        "title_size": 10,
        "text_size": 9
    }
}


# APP SETTINGS
# ///////////////////////////////////////////////////////////////
class Settings(object):
    # APP PATH
    # ///////////////////////////////////////////////////////////////

    # INIT SETTINGS
    # ///////////////////////////////////////////////////////////////
    def __init__(self):
        super(Settings, self).__init__()

        # DICTIONARY WITH SETTINGS
        # Just to have objects references
        self.items = settings
