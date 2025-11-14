import subprocess

class Groups:
    """
    
    """
    def __init__(self):
        """
        
        """
        
    def group_exists(self, group_name):
        """
        
        """
        return subprocess.run(["getent", "group", group_name]).returncode == 0

    def add_group(self, group_name):
        """
        
        """
        result = subprocess.run(["sudo", "addgroup", group_name],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
        return result.returncode == 0

    def add_user_to_group(self, user_name, group_name):
        """
        
        """
        result = subprocess.run(["sudo", "usermod", "-aG", group_name, user_name],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
        return result.returncode == 0

    def remove_user_from_group(self, user_name, group_name):
        """
        
        """
        result = subprocess.run(["sudo", "gpasswd", "-d", user_name, group_name],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
        return result.returncode == 0

    def delete_group(self, group_name):
        """
        
        """
        result = subprocess.run(["sudo", "delgroup", group_name],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
        return result.returncode == 0