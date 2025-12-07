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
                            {"name": "username", "type": str,
                                "help": "Username to search for user"}
                        ]
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
                self.utilities.show_existing_users()
            case ("utilities", "find-user"):
                self.utilities.find_by_username(username=args.username)