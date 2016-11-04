from enum import Enum

class ResultType(Enum):
    OK = 1
    FAIL = 2
    COMPILATION_ERROR = 3

def run_test(code_folder_path, test_input_folder_path, test_output_folder_path):
