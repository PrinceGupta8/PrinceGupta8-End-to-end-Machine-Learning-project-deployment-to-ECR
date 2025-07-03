import os
import sys
from src.Exception import CustomException
from src.logger import logging
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split
from src.Components.data_transformation import DataTransformation
from src.Components.model_trainer import ModelTrainer

@dataclass 
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    row_data_path:str=os.path.join('artifacts','data.csv')
class DataIngestion:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
    def initiate_data_ingestion(self):
        try:
            df=pd.read_csv(r'C:\Users\Practice DA\2-ML\3- Module 48 Practice\Data\stud.csv')
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.data_ingestion_config.row_data_path,index=False,header=True)
            train_arr,test_arr=train_test_split(df,test_size=0.2,random_state=33)
            train_arr.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            test_arr.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)
            logging.info('data is divided in train and test')
            return (
                self.data_ingestion_config.train_data_path,self.data_ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation_object(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))