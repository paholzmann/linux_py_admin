import subprocess
import pandas as pd
from .logger import Logger

class Users:
    def __init__(self):
        """
        
        """

    def add_users(self, filepath):
        """
        python -m main manage-users add-users --input-path data/generated_data/test/None.csv
        """
        if filepath.endswith("csv"):
            df = pd.read_csv(filepath)
        elif filepath.endswith("json"):
            df = pd.read_json(filepath)
            df = df.T
        else:
            raise ValueError("Unsupported file format.")
        
        for index, row in df.iterrows():
            first_name = row["first_name"]
            last_name = row["last_name"]
            username = row["username"]
            email = row["email"]
            department = row["department"]
            password = row["password"]
        
            try:
                subprocess.run(
                    ["useradd", "-m", "-c", f"{first_name} {last_name}, {email}", username],
                    check=True
                )
                subprocess.run(
                    ["chpasswd"],
                    input=f"{username}:{password}",
                    text=True,
                    check=True
                )
            except subprocess.CalledProcessError as error:
                print(f"Error while creating user {username}: {error}")

    def delete_users(self, filepath):
        """
        python -m main manage-users delete-users --input-path data/generated_data/test/None.csv
        """
        if filepath.endswith("csv"):
            df = pd.read_csv(filepath)
        elif filepath.endswith("json"):
            df = pd.read_json(filepath)
            df = df.T
        else:
            raise ValueError("Unsupported file format.")
        for index, row in df.iterrows():
            username = row["username"]
            try:
                subprocess.run(
                    ["deluser", "--remove-home", username],
                    check=True
                )

            except subprocess.CalledProcessError as error:
                print(f"Error while deleting user {username}: {error}")

class SingleUsers:
    def __init__(self):
        """
        Docstring for __init__
        
        :param self: Description
        """
        self.logger = Logger(name="Single user management", log_file="app.log").logger

    def create_single_user(self, first_name, last_name, email, username, password):
        """
        python -m main manage-users create-single-user first_name last_name email username password
        Log into the debian server:
        docker exec -it -u username my_debian /bin/bash
        """
        try:
            self.logger.info(f"Creating user: {username}")
            subprocess.run(
                ["useradd", "-m", "-c", f"{first_name} {last_name}, {email}", username],
                check=True
            )
            subprocess.run(
                ["chpasswd"],
                input=f"{username}:{password}",
                text=True,
                check=True
            )
        except subprocess.CalledProcessError as error:
            self.logger.error(f"Error while creating user {username}: {error}")

    def delete_single_user(self, username):
        """
        python -m main manage-users delete-single-user username
        """
        try:
            self.logger.warning(f"Deleting user: {username}")
            subprocess.run(
                ["deluser", "--remove-home", username],
                check=True
            )

        except subprocess.CalledProcessError as error:
            self.logger.error(f"Error while deleting user {username}: {error}")

    def add_single_user_to_group(self, username, group_name):
        """
        Docstring for add_single_user_to_group
        
        :param self: Description
        :param username: Description
        """
        try:
            self.logger.info(f"Adding user: {username} to group: {group_name}")
            subprocess.run(
                ["usermod", "-aG", group_name, username],
                check=True
            )
        except subprocess.CalledProcessError as error:
            self.logger.error(f"Error while adding user: {username} to group: {group_name}: {error}")

    def remove_user_from_group(self, username, group_name):
        """
        Docstring for remove_user_from_group
        
        :param self: Description
        :param username: Description
        :param group_name: Description
        """
        try:
            self.logger.warning(f"Removing user: {username} from group: {group_name}")
            subprocess.run(
                ["gpasswd", "-d", username, group_name],
                check=True
            )
        except subprocess.CalledProcessError as error:
            self.logger.error(f"Error while removing user: {username} from group: {group_name}: {error}")