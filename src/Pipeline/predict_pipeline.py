import sys
import os
import pandas as pd
from src.Exception import CustomException
from src.logger import logging
from src.utils import load_object

class CustomData:
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        math_score:int,
        reading_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course
        self.math_score=math_score
        self.reading_score = reading_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "math_score":[self.math_score],
                "reading_score": [self.reading_score]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
class predictPipeline:
    def __init__(self):
        pass
    def Predict(self,features):
        try:
            model_path=os.path.join('artifacts','model.pkl')
            preprocessor_path=os.path.join('artifacts','processor.pkl')
            model=load_object(model_path)
            logging.info('Before preprocessing')
            preprocessor=load_object(preprocessor_path)
            data_scaled=preprocessor.transform(features)
            logging.info('After preprocessing')
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)