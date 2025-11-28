import pandas as pd
import random
import json
import os
from .logger import Logger


class GenerateUserData:
    def __init__(self):
        """
        Docstring for __init__
        
        :param self: Description
        """
        self.first_names = [
        "Emma", "Liam", "Olivia", "Noah", "Ava",
        "Elijah", "Sophia", "Lucas", "Isabella", "Mason",
        "Mia", "Logan", "Charlotte", "Ethan", "Amelia",
        "James", "Harper", "Benjamin", "Evelyn", "Alexander"
        ]
        self.last_names = [
            "Smith", "Johnson", "Williams", "Brown", "Jones",
            "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
            "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
            "Thomas", "Taylor", "Moore", "Jackson", "Martin"
        ]
        self.departments = [
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

    def generate_users(self, n=10):
        """
        Docstring for generate_users
        
        :param self: Description
        :param n: Description
        """
        users = {}
        for i in range(n):
            first_name = random.choice(self.first_names)
            last_name = random.choice(self.last_names)
            username = f"{first_name.lower()}.{last_name.lower()}"
            email = f"{username}@example.com"
            department = random.choice(self.departments)
            password = lambda length=5: "".join(random.choice("0123456789") for _ in range(length))
            users[i] = {
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "email": email,
                "department": department,
                "password": password()
            }

        return users
    
class FileHandler:
    """
    Docstring for FileHandler
    """
    def __init__(self):
        """
        Docstring for __init__
        
        :param self: Description
        """
        self.logger = Logger(name="Test", log_file="app.log").logger

    def convert_to_file(self, data, folder, filename, to_json=False, to_csv=False):
        """
        Docstring for convert_to_file
        
        :param self: Description
        :param data: Description
        :param filepath: Description
        :param json: Description
        :param csv: Description
        """
        folder_path = os.path.join("data", folder).replace("\\", "/")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            self.logger.info(f"Folder created: {folder_path}")
        else:
            self.logger.info(f"Folder already exists: {folder_path}")
        if to_json:
            json_path = os.path.join(folder_path, filename)
            with open(json_path, "w") as file:
                json.dump(data, file, indent=4)
                self.logger.info(f"JSON file saved in path: {json_path}")
        if to_csv:
            csv_path = f"{folder_path}/{filename}.csv"
            df = pd.DataFrame.from_dict(data, orient="index")
            df.to_csv(csv_path, index=False)
            self.logger.info(f"CSV file created in path: {csv_path}")

    def delete_files(self, folder, del_json=False, del_csv=False):
        """
        Delete every file in a folder.
        """
        folder_path = os.path.join("data", folder).replace("\\", "/")
        if not os.path.exists(folder_path):
            self.logger.warning(f"Folder: {folder_path} does not exist and no files can be deleted")
        if not os.listdir(folder_path):
            self.logger.error(f"Folder: {folder_path} is empty and thus no files can be deleted")
        for file in os.listdir(folder_path):
            if del_json:
                if file.endswith(".json"):
                    json_path = os.path.join(folder_path, file)
                    os.remove(json_path)
                    self.logger.info(f"JSON file deleted in path: {json_path}")
            if del_csv:
                if file.endswith(".csv"):
                    csv_path = os.path.join(folder_path, file)
                    os.remove(csv_path)
                    self.logger.info(f"CSV file deleted in path: {csv_path}")