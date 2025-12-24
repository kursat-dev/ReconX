import json
import os
from typing import Dict, Any

def save_report(data: Dict[str, Any], filename: str = "report.json"):
    """
    Save the reconnaissance data to a JSON file.
    """
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Report saved to {filename}")
    except Exception as e:
        print(f"Error saving report: {e}")
