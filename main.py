from src.data import GenerateUserData
from src.cli import CLI
from src.logger import Logger
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

logger = Logger(name="Test", log_file="app.log").logger
if __name__ == "__main__":
    main = Main()
    logger.info("Started programm")
    main.run_cli()