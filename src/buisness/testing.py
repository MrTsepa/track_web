from enum import Enum


class ResultType(Enum):
    OK = 1
    WRONG_ANSWER = 2
    COMPILATION_ERROR = 3


# def run_test(code_folder_path, test_input_folder_path, test_output_folder_path):
#     pass

def run_test(code, test):
    """
    :param code: text of python script
    :param test: object with text attributes input and output
    """
    import sys, StringIO
    inputIO = StringIO.StringIO(test.input)
    outputIO = StringIO.StringIO()
    sys.stdin = inputIO
    sys.stdout = outputIO
    exec(code)
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__
    if outputIO.getvalue() == test.output + '\n':
        result = ResultType.OK
    else:
        result = ResultType.WRONG_ANSWER

    inputIO.close()
    outputIO.close()

    print result
    return result