from .data import GenerateUserData, FileHandler
from .users import Users
from .logger import Logger
import argparse
import json


class CLI:
    def __init__(self):
        """
        Docstring for __init__
        
        :param self: Description
        """
        self.generate_user_data = GenerateUserData()
        self.file_handler = FileHandler()
        self.users = Users()
        self.logger = Logger(name="Test", log_file="app.log").logger
        self.parser = argparse.ArgumentParser(description="Main parser")
        self.subparser = self.parser.add_subparsers(dest="command")
        self.setup_generate_user_data_parser()

    def setup_generate_user_data_parser(self):
        """
        Docstring for setup_generate_user_data_parser
        
        :param self: Description

        Example:
            >>> python -m main generate-users 10 --output-path data/generated_data/test --json --csv
        """
        parser = self.subparser.add_parser(
            "generate-users",
            help="Generate bulk user data"
        )
        parser.add_argument(
            "n",
            type=int,
            help="Number of users to generate")
        
        parser.add_argument(
            "--output-path",
            help="Output file path"
        )
        parser.add_argument(
            "--json",
            action="store_true",
            help="Save output as JSON"
        )
        parser.add_argument(
            "--csv",
            action="store_true",
            help="Save output as CSV"
        )

    def setup_users_parser(self):
        """
        
        """
        parser = self.subparser.add_parser(
            "manage-users",
            help="Manage user data"
        )
        parser.add_argument(
            "action",
            choices=["add-users", "remove-users"],
            help="Action to perform: add or delete users"
        )
        parser.add_argument(
            "--input-path",
            help="Input file path"
        )

    def run_commands(self):
        """
        Docstring for run_commands
        
        :param self: Description
        """
        args = self.parser.parse_args()
        if args.command == "generate-users":
            data = self.generate_user_data.generate_users(args.n)
            self.logger.info(f"{args.n} users generated")
            if args.output_path:
                self.file_handler.convert_to_file(data=data, filepath=args.output_path, to_json=args.json, to_csv=args.csv)
                self.logger.info(f"{'JSON' if args.json else ''} {'CSV' if args.csv else ''} file(s) saved in {args.output_path}")
        elif args.command == "manage-users":
            if args.action == "add":
                self.users.add_users(args.input_path)
            elif args.action == "delete":
                self.users.delete_users(args.input_path)