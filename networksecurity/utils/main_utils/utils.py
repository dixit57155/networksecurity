import yaml
from networksecurity.exception.exception import NetworkSecurityException
import sys, os
from networksecurity.logging.logger import logging
import numpy as np
import pickle
import dill

def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns its contents as a dictionary.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        dict: The contents of the YAML file as a dictionary.

    Raises:
        NetworkSecurityException: If there is an error reading the file.
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e
    

def write_yaml_file(file_path:str, content:object ,replace :bool =False)->None:
    """
    Writes a dictionary to a YAML file.

    Args:
        file_path (str): The path to the YAML file.
        content (dict): The dictionary to write to the file.

    Raises:
        NetworkSecurityException: If there is an error writing to the file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            yaml.dump(content,file)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e