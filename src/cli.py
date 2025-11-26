from .data import GenerateUserData
import argparse

# python -m src.cli  generate_user_data generate-users 10 

class CLI:
    def __init__(self):
        """
        Docstring for __init__
        
        :param self: Description
        """
        self.generate_user_data = GenerateUserData()
        self.parser = argparse.ArgumentParser(description="Main parser")
        self.subparser = self.parser.add_subparsers(dest="command")
        self.setup_generate_user_data_parser()
        
    def setup_generate_user_data_parser(self):
        """
        Docstring for setup_generate_user_data_parser
        
        :param self: Description
        """
        generate_user_data_parser = self.subparser.add_parser(
            "generate_user_data",
            help="Generate bulk user data"
        )
        generate_user_data_parser.add_argument(
            "operation",
            choices=["generate-users"],
            help="Choose the desired operation"
        )
        generate_user_data_parser.add_argument("n", type=int, help="Number of users to generate")

    def run_commands(self):
        """
        Docstring for run_commands
        
        :param self: Description
        """
        args = self.parser.parse_args()
        if args.command == "generate_user_data":
            if args.operation == "generate-users":
                result = self.generate_user_data(args.n)
            print(result)