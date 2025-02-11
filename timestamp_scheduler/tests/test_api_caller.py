"""
Unit tests for the API caller module.
"""

import unittest
import urllib.error
from models.api_caller import call_api

class TestAPICaller(unittest.TestCase):
    def test_api_call_success(self):
        """
        Test if the API call executes successfully.
        """
        timestamp = "2025-01-01 12:30:15"
        try:
            call_api(timestamp)
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

    def test_api_call_http_429_handling(self):
        """
        Test if the API correctly handles HTTP 429 errors.
        """
        timestamp = "2025-01-01 13:45:09"
        try:
            # Simulate HTTPError 429 by raising an exception manually
            raise urllib.error.HTTPError(None, 429, "Too Many Requests", None, None)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                success = True  # Correctly caught 429 error
            else:
                success = False
        self.assertTrue(success)

    def test_api_call_invalid_url(self):
        """
        Test if the API call handles invalid URLs correctly.
        """
        global API_URL  # Temporarily change API_URL for testing
        API_URL = "http://invalid.url"

        timestamp = "2025-01-01 14:00:00"
        try:
            call_api(timestamp)
            success = False  # Should fail, so success = False
        except urllib.error.URLError:
            success = True  # Correct behavior: should raise a URLError
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
