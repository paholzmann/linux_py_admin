from .data import GenerateUserData, FileHandler
from .users import Users, SingleUsers
from .logger import Logger
from .groups import Groups
from .utilities import Utilities
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
        self.single_users = SingleUsers()
        self.groups = Groups()
        self.utilities = Utilities()
        self.logger = Logger(name="CLI", log_file="app.log").logger
        self.parser = argparse.ArgumentParser(description="Main parser")
        self.subparser = self.parser.add_subparsers(dest="command")
        self.setup_users_parser()

    def setup_users_parser(self):
        """

        """
        parser = self.subparser.add_parser(
            "manage-users",
            help="User management"
        )
        action_parser = parser.add_subparsers(
            dest="action",
            required=True
        )
        create_dummy_parser = action_parser.add_parser(
            "create-dummy-users",
            help="Create dummy users"
        )
        create_dummy_parser.add_argument(
            "n",
            type=int,
            help="Number of dummy users to create"
        )
        show_existing_parser = action_parser.add_parser(
            "show-existing-users",
            help="Show every existing user in the System"
        )
        find_user_parser = action_parser.add_parser(
            "find-user",
            help="Find user by username"
        )
        find_user_parser.add_argument(
            "username",
            type=str,
            help="User to find"
        )
        create_single_user_parser = action_parser.add_parser(
            "create-single-user",
            help="Create single user"
        )
        create_single_user_parser.add_argument(
            "first-name",
            type=str,
            help="First name of the user"
        )
        create_single_user_parser.add_argument(
            "last-name",
            type=str,
            help="Last name of the user"
        )
        create_single_user_parser.add_argument(
            "email",
            type=str,
            help="Email of the user"
        )
        create_single_user_parser.add_argument(
            "username",
            type=str,
            help="Username o the user"
        )
        create_single_user_parser.add_argument(
            "password",
            type=str,
            help="Password of the user"
        )
    def run_commands(self):
        """
        Docstring for run_commands
        
        :param self: Description
        """
        args = self.parser.parse_args()
        if args.command == "manage-users":
            if args.action == "create-dummy-users":
                dummy_users = self.utilities.create_dummy_users(n=args.n)
            elif args.action == "show-existing-users":
                self.utilities.show_existing_users()
            elif args.action == "find-user":
                self.utilities.find_by_username(username=args.username)
            elif args.action == "create-single-user":
                self.single_users.add_single_user(first_name=args.first_name, last_name=args.last_name, email=args.email,
                                                username=args.username, password=args.password)
                