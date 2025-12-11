import pandas as pd
import random
import json
import os
from .logger import Logger

class FileHandler:
    """
    Docstring for FileHandler
    """
    def __init__(self):
        """
        Docstring for __init__
        
        :param self: Description
        """
        self.logger = Logger(name="Test", log_file="app.log").logger

    def convert_to_file(self, data, folder, filename, to_json=False, to_csv=False):
        """
        Docstring for convert_to_file
        
        :param self: Description
        :param data: Description
        :param filepath: Description
        :param json: Description
        :param csv: Description
        """
        folder_path = os.path.join("data", folder).replace("\\", "/")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            self.logger.info(f"Folder created: {folder_path}")
        else:
            self.logger.info(f"Folder already exists: {folder_path}")
        if to_json:
            json_path = os.path.join(folder_path, f"{filename}.json")
            with open(json_path, "w") as file:
                json.dump(data, file, indent=4)
                self.logger.info(f"JSON file saved in path: {json_path}")
        if to_csv:
            csv_path = os.path.join(folder_path, f"{filename}.csv")
            df = pd.DataFrame.from_dict(data, orient="index")
            df.to_csv(csv_path, index=False)
            self.logger.info(f"CSV file created in path: {csv_path}")

    def delete_files(self, folder, del_json=False, del_csv=False):
        """
        Delete every file in a folder.
        """
        folder_path = os.path.join("data", folder).replace("\\", "/")
        if not os.path.exists(folder_path):
            self.logger.warning(f"Folder: {folder_path} does not exist and no files can be deleted")
            return
        files_exist = os.listdir(folder_path)
        if not files_exist:
            self.logger.error(f"Folder: {folder_path} is empty and thus no files can be deleted")
            return
        for file in os.listdir(folder_path):
            if del_json and file.endswith(".json"):
                json_path = os.path.join(folder_path, file)
                os.remove(json_path)
                self.logger.info(f"JSON file deleted in path: {json_path}")
            if del_csv and file.endswith(".csv"):
                csv_path = os.path.join(folder_path, file)
                os.remove(csv_path)
                self.logger.info(f"CSV file deleted in path: {csv_path}")