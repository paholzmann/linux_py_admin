import subprocess
import pandas as pd
from .logger import Logger

class Groups:
    def __init__(self):
        """
        
        """

    def show_existing_groups(self):
        """
        python -m main manage-groups show-existing
        """
        try:
            subprocess.run(
                ["cat", "/etc/group"],
                check=True
                )
        except subprocess.CalledProcessError as error:
            print(f"Error while displaying groups: {error}")

    def create_groups(self):
        """
        python -m main manage-groups create-groups
        """
        groups = ["Engineering",
                "Product",
                "Design",
                "Quality-Assurance",
                "Operations",
                "HR",
                "Marketing",
                "Sales",
                "Customer-Success",
                "Finance"]
        for group in groups:
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
        except subprocess.CalledProcessError as error:
            print(f"Error while creating group: {group}: {error}")
    
    def add_users_to_groups(self):
        """
        
        """
        