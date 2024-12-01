import sys

def error_message_detail(error,error_detail:sys):
    """
    This function generates a detailed error message including the error type, error message, and error details.
    """
    _,_,exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured python script name [[{0}] line number [{1}] error message [{2}]]".format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )
    
    return error_message



class AppException(Exception):
    def __init__(self,error_message,error_detail):
        super().__init__(error_message)
        self.error_detail = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message