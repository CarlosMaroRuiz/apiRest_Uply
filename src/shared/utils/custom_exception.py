class CustomAppException(Exception):
    def __init__(self, code_error: int, msg: str):
        self.code_error = code_error
        self.msg = msg