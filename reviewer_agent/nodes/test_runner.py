from tools.tests.test_runner import run_tests

def test_runner(state):

    output = run_tests()

    return {
        "test_results": output
    }