import json
import os
from pathlib import Path


CONFIG_PATH = Path(__file__).resolve().parents[2] / "config" / "endpoint.json"


class Functional_Param:

    @staticmethod
    def get_base_endpoint():
        with open(CONFIG_PATH) as json_file:
            endpoints = json.load(json_file)
            env = os.getenv("PYTEST_ENV", endpoints["environment"]["env"]).lower()
            return endpoints[env]["base_url"]
