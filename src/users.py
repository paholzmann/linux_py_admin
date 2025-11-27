import subprocess
import pandas as pd
from .logger import Logger

class Users:
    def __init__(self):
        """
        
        """

    def add_users(self, filepath):
        """
        
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
                    ["sudo", "useradd", "-m", "-c", f"{first_name} {last_name}, {email}", username],
                    check=True
                )
                subprocess.run(
                    ["sudo", "chpasswd"],
                    input=f"{username}:{password}",
                    text=True,
                    check=True
                )
            except subprocess.CalledProcessError as error:
                print(f"Error while creating user {username}: {error}")

    def delete_users(self, filepath):
        """
        
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
                    ["sudo", "deluser", "--remove-home", username]
                )

            except subprocess.CalledProcessError as error:
                print(f"Error while deleting user {username}: {error}")

    def show_existing_users(self):
        """
        
        """
        try:
            subprocess.run(
                ["cat", "/etc/passwd"]
            )
        except subprocess.CalledProcessError as error:
            print(f"Error while loading existing users: {error}")

Users().delete_users("data/generated_data/test.json")