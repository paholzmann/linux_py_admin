import pandas as pd
import random
import json

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

    def convert_to_file(self, data, filepath, to_json=False, to_csv=False):
        """
        Docstring for convert_to_file
        
        :param self: Description
        :param data: Description
        :param filepath: Description
        :param json: Description
        :param csv: Description
        """
        if to_json:
            with open(f"{filepath}.json", "w") as file:
                json.dump(data, file, indent=4)
        if to_csv:
            df = pd.DataFrame.from_dict(data, orient="index")
            df.to_csv(f"{filepath}.csv", index=False)

    def delete_files(self, folder):
        """
        Delete every file in a folder.
        """
        