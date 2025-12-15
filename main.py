import json
from agents.planner import plan
from agents.executor import execute
from agents.supervisor import evaluate

print("Starting Mobile QA Agent...\n")

with open("tests/qa_tests.json") as f:
    tests = json.load(f)

for test in tests:
    print(f"Running {test['id']}: {test['description']}")

    plan_result = plan(test["description"])
    execution_result = execute(plan_result, test["id"])
    verdict = evaluate(test, execution_result)

    print("Execution:", execution_result)
    print("Verdict:", verdict)
    print("-" * 40)



