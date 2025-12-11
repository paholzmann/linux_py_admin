import subprocess
import json
import pandas as pd
import random
from .logger import Logger
from .data_handler import FileHandler
class Users:
    def __init__(self):
        """
        
        """
        self.logger = Logger(name="Utilities", log_file="app.log").logger
        self.file_handler = FileHandler()

    def create_dummy_users(self, n, filename):
        """
        Funktion ist vollständig.

        python -m main manage-users create-dummy-users n
        """
        users = {}
        with open("config/data_config.json", "r", encoding="utf-8") as file:
            config_data = json.load(file)
        for i in range(n):
            first_name = random.choice(config_data["first_names"])
            last_name = random.choice(config_data["last_names"])
            username = f"{first_name.lower()}.{last_name.lower()}.{i}"
            email = f"{username}@example.com"
            department = random.choice(config_data["departments"])
            groups = config_data["groups"][department]
            seniority_level = random.choice(config_data["seniority_level"])
            def password(length=5): return "".join(random.choice("0123456789") for _ in range(length))
            users[i] = {
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "email": email,
                "department": department,
                "groups": groups,
                "seniority_level": seniority_level,
                "password": password()
            }
        self.logger.info(f"Generating {n} users")
        self.file_handler.convert_to_file(data=users, folder="custom_data", filename=filename)
        return users

    def add_bulk_users(self, filepath):
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