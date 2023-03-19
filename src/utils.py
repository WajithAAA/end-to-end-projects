import os
import sys

import numpy as np
import pandas as pd
from src.exceptions import CustomException
import dill

def save_objects(file_path, objects):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(objects, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
