from utils.alert_reader import AlertReader

class AlertLogic:
    def __init__(self, file_path):
        self.alert_reader = AlertReader(file_path)

    def get_alerts(self, month="all"):
        data = self.alert_reader.read_alerts(month)
        return data
