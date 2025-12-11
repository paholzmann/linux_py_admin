from src.cli import CLI
from src.logger import Logger
class Main:
    def __init__(self):
        """
        Docstring for __init__
        
        :param self: Description
        """

    def create_user_workflow(self):
        """
        Docstring for create_user_workflow
        
        :param self: Description
        """

logger = Logger(name="Test", log_file="app.log").logger
if __name__ == "__main__":
    main = Main()
    logger.info("Started programm")
    CLI().run_cli()