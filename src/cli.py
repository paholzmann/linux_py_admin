from .users import SingleUsers
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
                            {"name": "username", "type": str,"help": "Username to search for user"}
                        ]
                    },
                    {
                        "name": "show-existing-groups",
                        "help": "Show all groups",
                        "arguments": []
                    }
                ]
            }
        ]

    def setup_utilities_cli(self):
        """
        """
        for definition in self.definitions:
            parser = self.subparser.add_parser(
                definition["parser"], help=definition["help"])
            actions_parser = parser.add_subparsers(
                dest="action", required=True)
            for action in definition["actions"]:
                action_parser = actions_parser.add_parser(
                    action["name"], help=action["help"])
                for argument in action["arguments"]:
                    action_parser.add_argument(
                        argument["name"],
                        type=argument.get("type", str),
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