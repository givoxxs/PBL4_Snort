# # config/ubuntu_config.py
# class UbuntuConfig:
#     def __init__(self):
#         self.alert_file_path = "/var/log/snort/alert_csv.txt"
#         self.rule_file_path = "/etc/snort/rules/local.rules"
#         self.log_dir = "/var/log/snort/"

from config.settings import Settings

class UbuntuConfig(Settings):
    RULE_PATH = "/usr/local/etc/rules/local.rules"
    LOG_PATH = "/var/log/snort/alert_csv.txt"