import os
from config.settings import config

class FileModifier:
    def __init__(self, rules_path = config.RULES_PATH, settings_path="settings.txt"):
        self.rules_path = rules_path
        self.settings_path = settings_path

    def modify(self, new_content):
        with open(self.file_path, 'w') as file:
            file.write(new_content)

    def add_local_rule(self, new_rule):
        try:
            with open(self.rules_path, 'a') as file:
                file.write(new_rule + '\n')
            return "Rule added successfully"
        except PermissionError:
            return "Permission denied"
        except Exception as e:
            return f"Error occurred: {str(e)}"
        
    def read_sid(self):
        try:
            with open(self.settings_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    temp = line.split(":")
                    if temp[0] == "sid":
                        return int(temp[1])
        except Exception as e:
            return f"Error occurred: {str(e)}"
    
    def update_sid(self, new_sid):
        try:
            lines = []
            with open(self.settings_path, 'r') as file:
                lines = file.readlines()
            with open(self.settings_path, 'w') as file:
                for line in lines:
                    line = line.strip()
                    temp = line.split(":")
                    if temp[0] == "sid":
                        file.write(f"sid:{new_sid}\n")
                    else:
                        file.write(line + '\n')
            return "SID updated successfully"
        except PermissionError:
            return "Permission denied"
        except Exception as e:
            return f"Error occurred: {str(e)}"
    
    def reload_ufw(self):
        try:
            os.system("ufw disable")
            os.system("ufw enable")
            return "UFW reloaded successfully"
        except PermissionError:
            return "Permission denied"
        except Exception as e:
            return f"Error occurred: {str(e)}"
        
    def reload_snort(self, service="snort3-nids"):
        try:
            os.system(f"systemctl stop {service}")
            res = os.system(f"systemctl start {service}")
            return res
        except PermissionError:
            return "Permission denied"
        except Exception as e:
            return f"Error occurred: {str(e)}"
        
    def execute_ufw_command(self, command):
        try:
            # res = os.popen(f"ufw {command}").read()
            res = os.system(command).read()
            return res
        except PermissionError:
            return "Permission denied"
        except Exception as e:
            return f"Error occurred: {str(e)}"
 
# Example usage       
if __name__ == "__main__":
    fm = FileModifier()
    print(fm.add_local_rule("alert tcp any any -> any any (msg:\"Test Rule\"; sid:10000001; rev:001;)"))
    print(fm.read_sid())
    print(fm.update_sid(10000002))
    print(fm.reload_ufw())
    print(fm.reload_snort())
    print(fm.execute_ufw_command("ufw status"))