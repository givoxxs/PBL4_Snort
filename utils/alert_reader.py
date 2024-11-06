class AlertReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_alerts(self, month="all"):
        # Read and filter alerts based on the month
        with open(self.file_path, "r") as file:
            data = [line.strip().split(",") for line in file]
        return data  # Adjust filtering by month as needed
