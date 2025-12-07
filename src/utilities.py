import subprocess
import random
import pandas as pd
from .logger import Logger


class Utilities:
    def __init__(self):
        """
        Docstring for __init__
        
        :param self: Description
        """
        self.logger = Logger(name="Utilities", log_file="app.log").logger

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
        self.logger.info(f"Created {n} users with data: {list(users[0].keys())}")
        return users

    def show_existing_users(self):
        """
        python -m main manage-users show-existing
        """
        try:
            self.logger.info(f"Showing every existing user")
            subprocess.run(
                ["cut", "-d:", "-f1", "/etc/passwd"],
                check=True
            )
        except subprocess.CalledProcessError as error:
            self.logger.error(f"Error while loading every existing user: {error}")

    def find_by_username(self, username):
        """
        python -m main manage-users find-user username
        """
        try:
            self.logger.info(f"Searching for user: {username}")
            subprocess.run(
                ["grep", username, "/etc/passwd"],
                check=True
            )
        except subprocess.CalledProcessError as error:
            self.logger.error(f"Error while searching for user: {username}: {error}")