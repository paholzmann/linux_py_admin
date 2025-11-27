import subprocess
import pandas as pd

class Users:
    def __init__(self):
        """
        
        """

    def add_users(self, filepath):
        """
        
        """
        if filepath.endswith("csv"):
            df = pd.read_csv(filepath)
            print(df)
        elif filepath.endswith("json"):
            df = pd.read_json(filepath)
            df = df.T
            print(df)
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

Users().add_users("data/generated_data/test.json")