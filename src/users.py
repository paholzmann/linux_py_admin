import subprocess

class Users:
    """
    
    """
    def __init__(self):
        """
        
        """

    def user_exists(self, user_name):
        """
        
        """
        return subprocess.run(["getent", "passwd", user_name]).returncode == 0

    def create_user(self, user_name):
        """
        
        """
        if self.user_exists(user_name):
            return True
        result = subprocess.run(["sudo", "adduser", user_name],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
        return result.returncode == 0
    
    def delete_user(self, user_name):
        """
        
        """
        result = subprocess.run(["sudo", "deluser", "--remove-home", user_name],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
        return result.returncode == 0