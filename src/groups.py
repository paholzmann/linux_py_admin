import subprocess
import pandas as pd
from .logger import Logger

class Groups:
    def __init__(self):
        """
        
        """
        self.all_groups = ["Engineering",
                                    "Product",
                                    "Design",
                                    "Quality-Assurance",
                                    "Operations",
                                    "HR",
                                    "Marketing",
                                    "Sales",
                                    "Customer-Success",
                                    "Finance"]



    def create_groups(self):
        """
        python -m main manage-groups create-groups
        """

        for group in self.all_groups:
            try:
                subprocess.run(
                    ["addgroup", group],
                    check=True
                )
            except subprocess.CalledProcessError as error:
                print(f"Error while creating group {group}: {error}")

    def create_single_group(self, group):
        """
        
        """
        try:
            subprocess.run(
                ["addgroup", group],
                check=True
            )
            self.all_groups.append(group)
        except subprocess.CalledProcessError as error:
            print(f"Error while creating group: {group}: {error}")
    
    def delete_all_groups(self):
        """
        
        """
        for group in self.all_groups:
            try:
                subprocess.run(
                    ["groupdel", group]
                )
                self.all_groups.remove(group)
            except subprocess.CalledProcessError as error:
                print(f"Error while deleting group: {group}: {error}")

    def add_users_to_groups(self):
        """
        
        """

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