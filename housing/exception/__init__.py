import os
import sys

class HousingException(Exception):


    def __init__(self, error_message: Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message = HousingException.get_detailed_error_message(error_message=error_message,
                                                                        error_detail=error_detail
                                                                        )


    @staticmethod
    def get_detailed_error_message(error_message: Exception,error_detail:sys)->str:
        
        _,_,exec_tb = error_detail.exc_info()
        line_no=exec_tb.tb_frame.f_lineno
        file_name=exec_tb.tb_frame.f_code.co_filename

        message = f"Error occured in script: {file_name} at line number: [{line_no}]. Error message: {error_message}"

        return message

    def __str__(self) -> str:
        return self.error_message
    
    def __repr__(self) -> str:
        return HousingException.__name__.str()