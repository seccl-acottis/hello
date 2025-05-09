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

print(needs)
