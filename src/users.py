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