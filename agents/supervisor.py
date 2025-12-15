def evaluate(test, execution_result):
    """
    Evaluates execution result against expected outcome.
    """

    expected = test.get("expected")  # "PASS" or "FAIL"
    success = execution_result.get("success", False)

    # Expected PASS
    if expected == "PASS":
        if success:
            return {
                "result": "PASS",
                "reason": "Action executed successfully"
            }
        else:
            return {
                "result": "FAIL",
                "reason": "Execution failed"
            }

    # Expected FAIL
    if expected == "FAIL":
        if not success:
            return {
                "result": "FAIL",
                "reason": "Expected condition not met"
            }
        else:
            return {
                "result": "PASS",
                "reason": "Unexpected success"
            }

    # Fallback (should never happen)
    return {
        "result": "FAIL",
        "reason": "Invalid test expectation"
    }
