from enum import Enum


class ResultType(Enum):
    OK = 1
    WRONG_ANSWER = 2
    RUNTIME_ERROR = 3


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
    try:
        exec(code)
    except Exception:
        return ResultType.RUNTIME_ERROR
    else:
        if outputIO.getvalue() == test.output + '\n':
            return ResultType.OK
        else:
            return ResultType.WRONG_ANSWER
    finally:
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        inputIO.close()
        outputIO.close()
