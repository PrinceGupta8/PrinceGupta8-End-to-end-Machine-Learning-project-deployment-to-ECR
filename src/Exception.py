import sys
from src.logger import logging

def error_message_detatil(error,error_detail:sys):
    _,_,exc_tab=error_detail.exc_info()
    filename=exc_tab.tb_frame.f_code.co_filename
    error_message=f'Error occured in the file {filename}, at the line {exc_tab.tb_lineno}, the error message: {str(error)}'
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail: sys):
        super().__init__(error_message)
        self.error_message=error_message_detatil(error_message,error_detail)
    def __str__(self):
        return self.error_message
    











