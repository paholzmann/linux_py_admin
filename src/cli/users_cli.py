from ..users import SingleUsers
from ..logger import Logger
from ..utilities import Utilities
import argparse
import json

class UsersCLI:
    def __init__(self):
        """
        Docstring for __init__
        
        :param self: Description
        """
        self.logger = Logger(name="CLI", log_file="app.log").logger
