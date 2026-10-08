import os
import random


class CommonUtility:

    @staticmethod
    def get_custom_header():
        token = os.getenv("GOREST_TOKEN")
        header = {
            "Content-Type": "application/json",
        }

        if token:
            header["Authorization"] = f"Bearer {token}"

        return header

    @staticmethod
    def get_unique_email():
        random_number = random.randint(100, 99999999)
        email = f"test_automation{random_number}@gmail.com"
        return email
