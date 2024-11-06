class ThreatLogic:
    @staticmethod
    def safe_threat(index):
        # Mark threat as safe by index
        return f"Threat at index {index} marked as safe."

    @staticmethod
    def ignore_threat(index):
        return f"Threat at index {index} ignored."

    @staticmethod
    def limit_threat(index):
        return f"Threat at index {index} limited."

    @staticmethod
    def block_threat(index):
        return f"Threat at index {index} blocked."
