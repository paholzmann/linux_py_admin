from .users import Users
from .logger import Logger
from .utilities import Utilities
import argparse
import json


class CLI:
    def __init__(self):
        """
        Docstring for __init__
        
        :param self: Description
        """
        self.logger = Logger(name="CLI", log_file="app.log").logger
        self.utilities = Utilities()
        self.users = Users()
        self.parser = argparse.ArgumentParser(description="Main parser")
        self.subparser = self.parser.add_subparsers(dest="command")

        self.definitions = [
            {
                "parser": "utilities",
                "help": "Utility functions",
                "actions": [
                    {
                        "name": "show-existing-users",
                        "help": "Show all users",
                        "arguments": []
                    },
                    {
                        "name": "find-user",
                        "help": "Find a user by username",
                        "arguments": [
                            {"name": "username", "type": str, "help": "Username to search for user"}
                        ]
                    },
                    {
                        "name": "show-existing-groups",
                        "help": "Show all groups",
                        "arguments": []
                    },
                    {
                        "name": "find-group",
                        "help": "Find a group by groupname",
                        "arguments": [
                            {"name": "groupname", "type": str, "help": "Group name to search for group"}
                        ]
                    }
                ]
            },
            {
                "parser": "users",
                "help": "User functions",
                "actions": [
                    {
                        "name": "add-user",
                        "help": "Add one user",
                        "arguments": [
                            {"name": "first_name", "type": str, "help": "First name of user"},
                            {"name": "last_name", "type": str, "help": "Last name of user"},
                            {"name": "email", "type": str, "help": "Email of user"},
                            {"name": "username", "type": str, "help": "Username of user"},
                            {"name": "password", "type": str, "help": "Password of user"}
                        ]
                    },
                    {
                        "name": "delete-user",
                        "help": "Delete one user",
                        "arguments": [
                            {"name": "username", "type": str, "help": "Username of user to delete"}
                        ]
                    },
                    {
                        "name": "add-user-to-group",
                        "help": "Add a user to a group",
                        "arguments": [
                            {"name": "username", "type": str, "help": "Username of the user to add to the group"},
                            {"name": "groupname", "type": str, "help": "Groupname of the group to add the user to"}
                        ]
                    },
                    {
                        "name": "remove-user-from-group",
                        "help": "Remove a user from a group",
                        "arguments": [
                            {"name": "username", "type": str, "help": "Username of the user to remove from the group"},
                            {"name": "groupname", "type": str, "help": "Groupname of the group to remove the user from"}
                        ]
                    }
                ]
            },
            {
                "parser": "groups",
                "help": "Group functions",
                "actions": [
                    {
                        "name": "add-group"
                    }
                ]
            }
        ]

    def setup_utilities_cli(self):
        """
        """
        type_mapping = {
            "str": str,
            "int": int,
            "float": float,
            "bool": bool
        }
        with open("config.json", "r", encoding="utf-8") as file:
            definitions = json.load(file)
        for definition in definitions:
            parser = self.subparser.add_parser(
                definition["parser"], help=definition["help"])
            actions_parser = parser.add_subparsers(
                dest="action", required=True)
            
            for action in definition["actions"]:
                action_parser = actions_parser.add_parser(
                    action["name"], help=action["help"])
                
                for argument in action["arguments"]:
                    arg_type = type_mapping.get(argument.get("type", "str"), str)
                    action_parser.add_argument(
                        argument["name"],
                        type=arg_type,
                        help=argument.get("help", "")
                    )

    def run_cli(self):
        """
        Docstring for run_cli
        
        :param self: Description
        """
        self.setup_utilities_cli()
        args = self.parser.parse_args()
        match (args.command, getattr(args, "action", None)):
            case ("utilities", "show-existing-users"):
                self.utilities.base_utility(logging_info="Showing every existing user",
                                            command=["cut", "-d:", "-f1", "/etc/passwd"], 
                                            logging_error="Error while loading every existing user")
            case ("utilities", "find-user"):
                self.utilities.base_utility(logging_info=f"Searching for user: {args.username}",
                                            command=["grep", args.username, "/etc/passwd"],
                                            logging_error=f"Error while searching for user: {args.username}")
            case ("utilities", "show-existing-groups"):
                self.utilities.base_utility(logging_info="Displaying every existing group",
                                            command=["cat", "/etc/group"],
                                            logging_error="Error while loading every existing group")
            case ("utilities", "find-group"):
                self.utilities.base_utility(logging_info=f"Searching for group: {args.groupname}",
                                            command=["getent", "group", args.groupname],
                                            logging_error=f"Error while searching for group: {args.groupname}")
            case ("users", "add-user"):
                self.utilities.base_utility(logging_info=f"Creating user: {args.username}",
                                            command=["useradd", "-m", "-c", f"{args.first_name} {args.last_name}, {args.email}", args.username])
                self.utilities.base_utility(logging_info=f"Setting password for user: {args.username}",
                                            command=["chpasswd"],
                                            input_data=f"{args.username}:{args.password}",
                                            text_data=True,
                                            logging_error=f"Error while setting up password for user: {args.username}")
            case ("users", "delete-user"):
                self.utilities.base_utility(logging_warning=f"Deleting user: {args.username}",
                                            command=["deluser", "--remove-home", args.username],
                                            logging_error=f"Error while deleting user: {args.username}")
            case ("users", "add-user-to-group"):
                self.utilities.base_utility(logging_info=f"Adding user: {args.username} to group: {args.groupname}",
                                            command=["usermod", "-aG", args.groupname, args.username],
                                            logging_error=f"Error while adding user: {args.username} to group: {args.groupname}")
            case ("users", "remove-user-from-group"):
                self.utilities.base_utility(logging_warning=f"Removing user: {args.username} from group: {args.groupname}",
                                            command=["gpasswd", "-d", args.username, args.groupname],
                                            logging_error=f"Error while removing user: {args.username} from group: {args.groupname}")
