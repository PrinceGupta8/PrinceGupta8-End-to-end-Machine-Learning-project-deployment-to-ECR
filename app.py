import sys
import os
from src.Pipeline.predict_pipeline import CustomData,predictPipeline
import pandas as pd
from src.Exception import CustomException
from src.logger import logging
from flask import Flask
from flask import render_template,redirect,request


application=Flask(__name__)
app=application
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    try:
        if request.method=='GET':
            return render_template('home.html')
        else:
            data=CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                math_score=float(request.form.get('math_score')),
                reading_score=float(request.form.get('reading_score'))
                )
            preds_df=data.get_data_as_data_frame()
            logging.info('data is converted to dataframe')
            pipeline=predictPipeline()
            result=pipeline.Predict(preds_df)
            logging.info('prediction is completed!')
            return render_template('home.html',results=result[0])
    except Exception as e:
        raise CustomException(e,sys)
    

if __name__=='__main__':
    app.run(host="0.0.0.0")
