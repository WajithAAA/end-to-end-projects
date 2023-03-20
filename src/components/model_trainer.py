import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
     AdaBoostRegressor,
     GradientBoostingRegressor,
     RandomForestRegressor
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exceptions import CustomException
from src.logger import logging

from src.utils import save_objects, evaluated_model

@dataclass
class ModelTrainingConfig:
    trained_model_path = os.path.join("artifacts", "model.pkl")


class ModelTraining:
    def __init__(self):
        self.model_trainer_path = ModelTrainingConfig()

    def initiate_model_trainer(self, train_array, test_array):

        try:
            print("Starting data training...")


            logging.info("Spliting training and testing data")

            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            ) 

            models = {
                "RandomForest": RandomForestRegressor(),
                "DecisionTree": DecisionTreeRegressor(),
                "Gradient Boost": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "K-NearestNeighbors": KNeighborsRegressor(),
                "XGBooting Regressor": XGBRegressor(),
                "CatBoostingRegressor": CatBoostRegressor(),
                "AdamBoostingRegressor":AdaBoostRegressor(),
            }

            model_report:dict = evaluated_model(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test , models=models)

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No Best Model found")
            logging.info("Best Model found: %s using train and test data", best_model)


            save_objects(file_path=self.model_trainer_path.trained_model_path,
                         objects=best_model
                         )
            
            predicted_data = best_model.predict(X_test)

            r_square = r2_score(y_test,predicted_data)

            return {
                "best_model":best_model_name,
                "r2_score": r_square
            }


        except Exception as e:
            logging.info("Model trainer found exception")
            raise CustomException(e, sys)