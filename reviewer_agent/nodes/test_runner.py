from tools.tests.test_runner import run_tests
from tools.tests.test_formatter import format_test_results


def test_runner(state):

    results = run_tests()

    formatted = format_test_results(results)

    print("=== TEST RESULTS ===")
    print(formatted)

    return {
        "test_results": formatted
    }