from .data import GenerateUserData, FileHandler
from .users import Users, SingleUsers
from .logger import Logger
from .groups import Groups, SingleGroups
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
        self.single_groups = SingleGroups()
        self.utilities = Utilities()
        self.logger = Logger(name="CLI", log_file="app.log").logger
        self.parser = argparse.ArgumentParser(description="Main parser")
        self.subparser = self.parser.add_subparsers(dest="command")
        self.setup_users_parser()
        self.setup_groups_parser()

# ------------------------- USERS -------------------------
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
        self.create_dummy_parser(action_parser=action_parser)
        self.show_existing_parser(action_parser=action_parser)
        self.find_user_parser(action_parser=action_parser)
        self.create_single_user_parser(action_parser=action_parser)
        self.delete_single_user_parser(action_parser=action_parser)

    def create_dummy_parser(self, action_parser):
        """
        Docstring for create_dummy_parser
        
        :param self: Description
        :param action_parser: Description
        """
        parser = action_parser.add_parser(
            "create-dummy-users",
            help="Create dummy users"
        )
        parser.add_argument(
            "n",
            type=int,
            help="Number of dummy users to create"
        )
        return parser

    def show_existing_parser(self, action_parser):
        """
        Docstring for show_existing_parser
        
        :param self: Description
        :param action_parser: Description
        """
        parser = action_parser.add_parser(
            "show-existing-users",
            help="Show every existing user in the System"
        )
        return parser

    def find_user_parser(self, action_parser):
        """
        Docstring for find_user_parser
        
        :param self: Description
        :param action_parser: Description
        """
        parser = action_parser.add_parser(
            "find-user",
            help="Find user by username"
        )
        parser.add_argument(
            "username",
            type=str,
            help="User to find"
        )
        return parser

    def create_single_user_parser(self, action_parser):
        """
        Docstring for create_single_user_parser
        
        :param self: Description
        :param action_parser: Description
        """
        parser = action_parser.add_parser(
            "create-single-user",
            help="Create single user"
        )
        parser.add_argument(
            "first_name",
            type=str,
            help="First name of the user"
        )
        parser.add_argument(
            "last_name",
            type=str,
            help="Last name of the user"
        )
        parser.add_argument(
            "email",
            type=str,
            help="Email of the user"
        )
        parser.add_argument(
            "username",
            type=str,
            help="Username of the user"
        )
        parser.add_argument(
            "password",
            type=str,
            help="Password of the user"
        )
        return parser

    def delete_single_user_parser(self, action_parser):
        """
        Docstring for delete_single_user_parser
        
        :param self: Description
        """
        parser = action_parser.add_parser(
            "delete-single-user",
            help="Delete single user by username"
        )
        parser.add_argument(
            "username",
            type=str,
            help="Username of the user to delete"
        )
        return parser
# ------------------------- GROUPS -------------------------
    def setup_groups_parser(self):
        """
        Docstring for setup_groups_parser
        
        :param self: Description
        """
        parser = self.subparser.add_parser(
            "manage-groups",
            help="Group management"
        )
        action_parser = parser.add_subparsers(
            dest="action",
            required=True
        )
        self.show_existing_groups_parser(action_parser=action_parser)
    
    def show_existing_groups_parser(self, action_parser):
        """
        Docstring for show_existing_groups_parser
        
        :param self: Description
        """
        parser = action_parser.add_parser(
            "show-existing-groups",
            help="Show existing groups"
        )
        return parser
    
    def create_single_group_parser(self, action_parser):
        """
        Docstring for create_single_group_parser
        
        :param self: Description
        :param action_parser: Description
        """
        parser = action_parser.add_parser(
            "create-single-group",
            help="Create a single group"
        )
        parser.add_argument(
            "group_name",
            type=str,
            help="Group name to create group"
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
                self.single_users.create_single_user(first_name=args.first_name, last_name=args.last_name, email=args.email,
                                                username=args.username, password=args.password)
            elif args.action == "delete-single-user":
                self.single_users.delete_single_user(username=args.username)
        
        elif args.command == "manage-groups":
            if args.action == "show-existing-groups":
                self.utilities.show_existing_groups()
            elif args.action == "create-single-group":
                self.single_groups.create_single_group(group_name=args.group_name)