from src.buisness.testing import run_test


def execute(code, tests):
    results = []
    for test in tests:
        results.append(run_test(code, test))
    return results