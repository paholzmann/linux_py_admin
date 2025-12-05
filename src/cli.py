from .data import GenerateUserData, FileHandler
from .users import Users
from .logger import Logger
from .groups import Groups
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
        self.groups = Groups()
        self.logger = Logger(name="Test", log_file="app.log").logger
        self.parser = argparse.ArgumentParser(description="Main parser")
        self.subparser = self.parser.add_subparsers(dest="command")
        self.setup_generate_user_data_parser()
        self.setup_users_parser()
        self.setup_delete_files_parser()
        self.setup_groups_parser()

    def setup_generate_user_data_parser(self):
        """
        Docstring for setup_generate_user_data_parser
        
        :param self: Description

        Example:
            >>> python -m main generate-users 10 --folder generated_data/test --json --csv
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
            "--folder",
            help="Output folder name"
        )
        parser.add_argument(
            "--filename",
            help="Output filename"
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

    def setup_delete_files_parser(self):
        """
        
        """
        parser = self.subparser.add_parser(
            "delete-files",
            help="Delete all files in a directory"
        )
        parser.add_argument(
            "--folder",
            help="Directory path"
        )
        parser.add_argument(
            "--json",
            action="store_true",
            help="Delete every JSON file"
        )
        parser.add_argument(
            "--csv",
            action="store_true",
            help="Delete every CSV file"
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
            choices=["add-users", "delete-users", "show-existing"],
            help="Action to perform: add or delete users"
        )
        parser.add_argument(
            "--input-path",
            help="Input file path"
        )
    def setup_groups_parser(self):
        """
        python -m manage-groups show-existing
        """
        parser = self.subparser.add_parser(
            "manage-groups",
            help="Manage groups"
        )
        action_parser = parser.add_subparsers(
            dest="action",
            required=True
        )
        show_parser = action_parser.add_parser(
            "show-existing",
            help="Show existing groups"
        )
        create_groups_parser = action_parser.add_parser(
            "create-groups",
            help="Create basic groups"
        )
        create_single_group_parser = action_parser.add_parser(
            "create-single-group",
            help="Create custom single groups"
        )
        create_single_group_parser.add_argument(
            "group",
            type=str,
            help="Group name to create group"
        )
        delete_all_groups_parser = action_parser.add_parser(
            "delete-all-groups",
            help="Delete all custom created groups"
        )
        delete_single_group_parser = action_parser.add_parser(
            "delete-single-group",
            help="Delete a single group"
        )
        delete_single_group_parser.add_argument(
            "group",
            type=str,
            help="Group name to delete group"
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
            if args.folder:
                self.file_handler.convert_to_file(data=data, folder=args.folder, filename=args.filename ,to_json=args.json, to_csv=args.csv)
        elif args.command == "manage-users":
            if args.action == "add-users":
                self.users.add_users(args.input_path)
            elif args.action == "delete-users":
                self.users.delete_users(args.input_path)
            elif args.action == "show-existing":
                self.users.show_existing_users()

        elif args.command == "delete-files":
            self.file_handler.delete_files(folder=args.folder, del_json=args.json, del_csv=args.csv)
        
        elif args.command == "manage-groups":
            if args.action == "show-existing":
                self.groups.show_existing_groups()
            elif args.action == "create-groups":
                self.groups.create_groups()
            elif args.action == "create-single-group":
                self.groups.create_single_group(group=args.group)
            elif args.action == "delete-all-groups":
                self.groups.delete_all_groups()
            elif args.action == "delete-single-group":
                self.groups.delete_single_group(group=args.group)