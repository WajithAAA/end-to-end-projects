import os
import sys
from src.exceptions import CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split
import pandas as pd
from dataclasses import dataclass

from src.components.data_transformation import DataTransformationConfig
from src.components.data_transformation import DataTransformation

from src.components.model_trainer import ModelTrainingConfig
from src.components.model_trainer import ModelTraining


@dataclass
class DataIngestionConfig:

    train_data_path : str=os.path.join("artifacts", "train.csv")
    test_data_path : str=os.path.join("artifacts", "test.csv")
    raw_data_path : str=os.path.join("artifacts", "data.csv")
   


class DataIngestion:
    '''
        This is class is responsible for Data Ingestion
    '''

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Starting data ingestion method")

        try:
            print("Starting data ingestion method")
            
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path,
            )

        except Exception as e:
            logging.info("Ingestion is not completed")
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data, raw_data = obj.initiate_data_ingestion()

    data_transformer = DataTransformation()
    train_arr, test_arr,_ = data_transformer.initiate_data_transformation(train_data, test_data)

    model_trainer = ModelTraining()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))


            