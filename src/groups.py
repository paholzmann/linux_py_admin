import subprocess
import pandas as pd
from .logger import Logger

class SingleGroups:
    def __init__(self):
        """
        Docstring for __init__
        
        :param self: Description
        """
        self.logger = Logger(name="Utilities", log_file="app.log").logger
    
    def create_single_group(self, group_name):
        """
        Docstring for create_single_group
        
        :param self: Description
        :param group_name: Description
        """
        try:
            self.logger.info(f"Creating group: {group_name}")
            subprocess.run(
                ["addgroup", group_name],
                check=True
            )
        except subprocess.CalledProcessError as error:
            self.logger.error(f"Error while creating group {group_name}: {error}")

    def delete_single_group(self, group_name):
        """
        Docstring for delete_single_group
        
        :param self: Description
        :param group_name: Description
        """
        try:
            self.logger.warning(f"Deleting group: {group_name}")
            subprocess.run(
                ["groupdel", group_name]
            )
        except subprocess.CalledProcessError as error:
            self.logger.error(f"Error while deleting single group: {group_name}: {error}")