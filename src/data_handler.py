import random
import pandas as pd # type: ignore

class CreateData:
    """
    
    """
    def __init__(self):
        """
        
        """
        self.input_folder = "data/input"
        self.output_folder = "data/output"
        self.first_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia",
               "Kevin", "Laura", "Michael", "Nina", "Oliver", "Paula", "Quentin", "Rachel", "Steve", "Tina",
               "Uma", "Victor", "Wendy", "Xander", "Yara", "Zane"]

        self.last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin",
              "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Lewis", "Lee", "Walker", "Hall", "Allen"]

        self.roles = ["Junior", "Senior", "Lead", "Manager", "Intern", "Engineer", "Specialist", "Coordinator", "Analyst"]

        self.departments = [
            "IT", "Support", "ML", "WebDev", "Data", "Marketing", "Social Media",
            "Design", "Branding", "Email", "Sales", "HR", "Finance", "Operations", "R&D", "Security"
        ]

    def generate_random_data(self, n=100):
        """
        
        """
        users = {}
        for i in range(n):
            first_name = random.choice(self.first_names)
            last_name = random.choice(self.last_names)
            role = random.choice(self.roles)
            department = random.choice(self.departments)
            username = f"{first_name.lower()}.{last_name.lower()}{i}"
            email = f"{username}@example.com"
            users[i] = {
                "First name": first_name,
                "Last name": last_name,
                "Role": role,
                "Department": department,
                "Username": username,
                "Email": email
            }
        return users
    
    def create_csv(self, data, filename):
        """
        
        """
        df = pd.DataFrame(data)
        df = df.T
        df.columns = ["First name", "Last name", "Role", "Department", "Username", "Email"]
        df = df.reset_index(drop=True)
        df.to_csv(f"{self.input_folder}/{filename}")
    
class GetData:
    """
    
    """
    def __init__(self):
        """
        
        """