import os
import sys
from sklearn.metrics import r2_score
import pickle
from src.Exception import CustomException
from src.logger import logging
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        logging.info(f"{obj} is saved")
        raise CustomException(e,sys)

def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info(f'{file_path} is loaded')
        raise CustomException(e,sys)

def evaluate_model(x_train,y_train,x_test,y_test,models,params):
    try:
        report={}
        for i in range(len(list(models))):
            model=list(models.values())[i]
            param=params[list(params.keys())[i]]

            rs=RandomizedSearchCV(model,param,cv=3)
            rs.fit(x_train,y_train)

            model.set_params(**rs.best_params_)
            model.fit(x_train,y_train)

            y_pred=model.predict(x_test)
            score=r2_score(y_test,y_pred)
            report[list(models.keys())[i]]=score
        return report
    except Exception as e:
        CustomException(e,sys)


