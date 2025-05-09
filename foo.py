import os
import json
from typing import Dict, Any

#os.environ["NEEDS"] = """{
#    "imSkipped": {
#      "result": "skipped",
#      "outputs": {}
#    },
#    "imFailing": {
#      "result": "failure",
#      "outputs": {}
#    }
#}"""

if os.getenv

print(os.environ.get("NEEDS"))
needs: Dict[str, Any] = json.loads(os.environ.get("NEEDS"))
failed = False

for k, v in needs.items():
    if v["result"] == "failure":
        print(f"Failing pipeline because job {k} failed")
        failed = True
        break


if failed:
    exit(1)
