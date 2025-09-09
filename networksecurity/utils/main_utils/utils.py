from sklearn.metrics import r2_score
import yaml
from networksecurity.exception.exception import NetworkSecurityException
import sys, os
from networksecurity.logging.logger import logging
import numpy as np
import pickle
import dill

from sklearn.model_selection import GridSearchCV

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
    

def save_numpy_array_data(file_path: str, array: np.array) -> None:
    """
    Save a numpy array to a file.

    Args:
        file_path (str): The path to the file where the array will be saved.
        array (np.array): The numpy array to save.

    Raises:
        NetworkSecurityException: If there is an error saving the array.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e   
    

def save_object(file_path: str, obj: object) -> None:
    """
    Save a Python object to a file using dill.

    Args:
        file_path (str): The path to the file where the object will be saved.
        obj (object): The Python object to save.

    Raises:
        NetworkSecurityException: If there is an error saving the object.
    """
    try:
        logging.info(f"Saving object to {file_path}")
        # dir_path = os.path.dirname(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
        logging.info(f"Object saved to {file_path} successfully")
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e
    

def load_object(file_path: str) -> object:
    """
    Load a Python object from a file using dill.

    Args:
        file_path (str): The path to the file from which the object will be loaded.

    Returns:
        object: The loaded Python object.

    Raises:
        NetworkSecurityException: If there is an error loading the object.
    """
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} does not exist")
        with open(file_path, 'rb') as file_obj:
            print(file_obj)
            return pickle.load(file_obj)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e
    


def load_numpy_array_data(file_path: str) -> np.array:
    """
    Load a numpy array from a file.

    Args:
        file_path (str): The path to the file from which the array will be loaded.

    Returns:
        np.array: The loaded numpy array.

    Raises:
        NetworkSecurityException: If there is an error loading the array.
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e
    

def evaluate_models(X_train , y_train , X_test , y_test , models :dict , params :dict)->dict:
    try:
        report ={}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = params[list(models.keys())[i]]

            gs =GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)


            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score
        return report
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e