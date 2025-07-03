import sys 
import os
from src.Exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor,AdaBoostRegressor
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from src.utils import evaluate_model,save_object
from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join('artifacts','model.pkl')
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
    def initiate_model_trainer(self,train_array,test_array):
        try:
            x_train,y_train,x_test,y_test=train_array[:,:-1],train_array[:,-1],test_array[:,:-1],test_array[:,-1]
            models={
                'Linear Regression':LinearRegression(),
                'Decision Tree':DecisionTreeRegressor(),
                'KNeighborsRegressor':KNeighborsRegressor(),
                'svr':SVR(),
                'RandomForestRegressor':RandomForestRegressor(),
                'GradientBoostingRegressor':GradientBoostingRegressor(),
                'AdaBoostRegressor':AdaBoostRegressor(),
                'CatBoostRegressor':CatBoostRegressor(),
                'XGBRegressor':XGBRegressor()
            }
            params = {
    'Linear Regression': {},  # No hyperparameters for basic LinearRegression

    'Decision Tree': {
        'criterion': ['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
        'splitter': ['best', 'random'],
        'max_depth': [None, 5, 10, 20, 50],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    },

    'KNeighborsRegressor': {
        'n_neighbors': [3, 5, 7, 10],
        'weights': ['uniform', 'distance'],
        'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']
    },

    'SVR': {
        'kernel': ['rbf', 'linear', 'poly'],
        'C': [0.1, 1, 10],
        'epsilon': [0.01, 0.1, 0.2]
    },

    'RandomForestRegressor': {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20, 50],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2]
    },

    'GradientBoostingRegressor': {
        'learning_rate': [0.01, 0.05, 0.1],
        'n_estimators': [100, 200],
        'subsample': [0.6, 0.8, 1.0],
        'max_depth': [3, 5, 10]
    },

    'AdaBoostRegressor': {
        'n_estimators': [50, 100, 200],
        'learning_rate': [0.01, 0.1, 1.0],
        'loss': ['linear', 'square', 'exponential']
    },

    'CatBoostRegressor': {
        'iterations': [100, 200],
        'learning_rate': [0.01, 0.05, 0.1],
        'depth': [4, 6, 10]
    },

    'XGBRegressor': {
        'n_estimators': [100, 200],
        'learning_rate': [0.01, 0.05, 0.1],
        'max_depth': [3, 5, 10],
        'subsample': [0.6, 0.8, 1.0]
    }
}
            model_report:dict=evaluate_model(x_train,y_train,x_test,y_test,models,params)
            best_model_score=max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model=models[best_model_name]
            if best_model_score<0.6:
                raise CustomException('No best model')
            logging.info('Best model is found')
            save_object(self.model_trainer_config.trained_model_file_path,obj=best_model)
            print(best_model_score)
            return best_model
        except Exception as e:
            raise CustomException(e,sys)
        
