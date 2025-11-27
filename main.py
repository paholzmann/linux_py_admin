from src.data import GenerateUserData
from src.cli import CLI

class Main:
    def __init__(self):
        """
        Docstring for __init__
        
        :param self: Description
        """
        self.generate_user_data = GenerateUserData()
        self.cli = CLI()

    def create_user_workflow(self):
        """
        Docstring for create_user_workflow
        
        :param self: Description
        """
        
    def run_cli(self):
        """
        Docstring for run_cli
        
        :param self: Description

    
        Example:
            >>> python -m main generate-user-data generate-users 10
            >>> 
        """
        self.cli.run_commands()

if __name__ == "__main__":
    main = Main()
    main.run_cli()