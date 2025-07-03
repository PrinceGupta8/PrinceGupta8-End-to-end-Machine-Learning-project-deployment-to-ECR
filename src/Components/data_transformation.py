import sys
import os
from src.logger import logging
from src.Exception import CustomException
from src.utils import save_object
from  sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from  sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocesing_data_file_path=os.path.join('artifacts','processor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_tranformation_config=DataTransformationConfig()
    def get_data_transformation_object(self):
        try:
            numerical_columns = ["math_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            num_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )
            cat_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('ohe',OneHotEncoder(handle_unknown='ignore')),
                    ('scaler',StandardScaler(with_mean=False))
                ]
            )
            preprocessor=ColumnTransformer(
                [
                    ('num_col',num_pipeline,numerical_columns),
                    ('cat_col',cat_pipeline,categorical_columns)
                ]
            )
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
    def initiate_data_transformation_object(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            target_column='writing_score'

            input_train_df=train_df.drop(target_column,axis=1)
            target_train_df=train_df[target_column]

            input_test_df=test_df.drop(target_column,axis=1)
            target_test_df=test_df[target_column]
            
            preprocessor=self.get_data_transformation_object()
            
            input_train_df=preprocessor.fit_transform(input_train_df)
            input_test_df=preprocessor.transform(input_test_df)
            
            train_arr=np.c_[input_train_df,np.array(target_train_df)]
            test_arr=np.c_[input_test_df,np.array(target_test_df)]

            save_object(self.data_tranformation_config.preprocesing_data_file_path,obj=preprocessor)
            logging.info('Model is saved')
            return (train_arr,test_arr,self.data_tranformation_config.preprocesing_data_file_path)
        except Exception as e:
            raise CustomException(e,sys)
