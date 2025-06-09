import unittest
from src.email_validation.util import *

class TestEmailValidation(unittest.TestCase):
    def test_email_validation(self):
            test_cases = [
                {
                    "input": [
                        "john.doe@example.com",
                        "jane-doe@mysite.net",
                        "invalid.email@.com",
                        "bob_smith@mail.org",
                        "carol123@mail",
                        "good_email-123@mail.com"],
                    "input": [
                        "plainaddress",
                        "@missingusername.com",
                        "username@.com",
                        "valid.email1@mail.com",
                        "valid.email2@mail.co"
            ],
                    "expected": [
                        "valid.email1@mail.com",
                        "valid.email2@mail.co"
            ]
            },
            {
                "input": [],
                "expected": []
            }
            ]
if __name__ == "__main__":
    unittest.main()
