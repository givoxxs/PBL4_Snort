import os
from pathlib import Path
import platform

class Settings:
    APP_TITLE = "Quản trị mạng"
    APP_WIDTH = 600
    APP_HEIGHT = 400
    LOG_PATH = "/var/log/snort/alert_csv.txt"
    RULE_PATH = "/etc/snort/rules/local.rules"

    @staticmethod
    def load_config():
        if os.name == 'nt':
            from .windows_config import WindowsConfig
            return WindowsConfig()
        else:
            from .ubuntu_config import UbuntuConfig
            return UbuntuConfig()

config = Settings.load_config()
