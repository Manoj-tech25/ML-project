import sys
from src.logger import logger

def error_message_details(error, error_details: sys):
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    message = f"Error occurred in [{file_name}], line [{line_no}]: {str(error)}"
    logger.error(message)
    return message

class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details)

    def __str__(self):
        return self.error_message




from src.logger import logging
from src.exception import CustomException
import sys

if __name__ == "__main__":
    try:
        x = 1 / 0
    except Exception as e:
        logging.info("div by 0")
        raise CustomException(e, sys)