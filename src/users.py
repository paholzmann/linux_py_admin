import subprocess
import pandas as pd
import random
from .logger import Logger

class Users:
    def __init__(self):
        """
        
        """
        self.logger = Logger(name="Utilities", log_file="app.log").logger

    def create_user(self, first_name, last_name, email, username, password):
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

    def create_dummy_users(self, n):
        """
        Funktion ist vollständig.

        python -m main manage-users create-dummy-users n
        """
        first_names = [
            "Emma", "Liam", "Olivia", "Noah", "Ava",
            "Elijah", "Sophia", "Lucas", "Isabella", "Mason",
            "Mia", "Logan", "Charlotte", "Ethan", "Amelia",
            "James", "Harper", "Benjamin", "Evelyn", "Alexander"
        ]
        last_names = [
            "Smith", "Johnson", "Williams", "Brown", "Jones",
            "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
            "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
            "Thomas", "Taylor", "Moore", "Jackson", "Martin"
        ]
        departments = [
            "Engineering",
            "Product",
            "Design",
            "Quality Assurance",
            "Operations",
            "Human Resources",
            "Marketing",
            "Sales",
            "Customer Success",
            "Finance"
        ]
        users = {}
        for i in range(n):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            username = f"{first_name.lower()}.{last_name.lower()}"
            email = f"{username}@example.com"
            department = random.choice(departments)

            def password(length=5): return "".join(
                random.choice("0123456789") for _ in range(length))
            users[i] = {
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "email": email,
                "department": department,
                "password": password()
            }
        self.logger.info(
            f"Created {n} users with data: {list(users[0].keys())}")
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