from typing import Dict, Any

needs: Dict[str, Any] = {
    "imSkipped": {
      "result": "skipped",
      "outputs": {}
    },
    "imFailing": {
      "result": "failure",
      "outputs": {}
    }
}

failed = False

for k, v in needs.items():
    if v["result"] == "failure":
        print(f"Failing pipeline because job {k} failed")
        failed = True
        break


if failed:
    exit(1)
