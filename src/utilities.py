import subprocess
import random
import pandas as pd
from .logger import Logger


class Utilities:
    def __init__(self):
        """
        Docstring for __init__
        
        :param self: Description
        """
        self.logger = Logger(name="Utilities", log_file="app.log").logger

    def base_utility(self, logging_info="", logging_warning="", command=[], input_data=None, text_data=False, logging_error=""):
        """
        Examples:
            >>> python -m main utilities show-existing-users
            >>> python -m main utilities find-user username
            >>> python -m main utilities show-existing-groups
            >>> 
        """
        try:
            if logging_info != "":
                self.logger.info(logging_info)
            if logging_warning != "":
                self.logger.warning(logging_warning)
            subprocess.run(
                command,
                input=input_data,
                text=text_data,
                check=True
            )
        except subprocess.CalledProcessError as error:
            self.logger.error(f"{logging_error}: {error}")