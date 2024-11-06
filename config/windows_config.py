# class WindowsConfig:
#     def __init__(self):
#         self.alert_file_path = "assets/alert_csv.txt"
#         self.rule_file_path = "assets/local.rules"
#         self.log_dir = "logs/"

from config.settings import Settings

class WindowsConfig(Settings):
    RULE_PATH = "assets/local.rules"
    LOG_PATH = "assets/alert_csv.txt"
