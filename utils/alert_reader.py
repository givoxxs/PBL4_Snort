class AlertReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_alerts(self, month="all"):
        alerts = []
        with open(self.file_path, "r") as file:
            lines = file.readlines()
            for line in lines[1:]:  # Skip header
                alert = self._parse_alert_line(line.strip())
                if month == "all" or alert[0][:2] == month:
                    alerts.append(alert)
        return alerts

    def _parse_alert_line(self, line):
        data = line.split(",")
        return (
            data[0], data[1], data[2], data[3], data[4], data[5], data[6],
            data[7], data[8], data[9], data[10], data[11]
        )
