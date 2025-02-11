"""
Unit test for scheduler with generated timestamps.
"""

import unittest
from models.scheduler import schedule_tasks
from test_generator import generate_test_timestamps

class TestScheduler(unittest.TestCase):
    def test_schedule_tasks_with_generated_timestamps(self):
        """
        Test if schedule_tasks can handle dynamically generated timestamps.
        """
        timestamps = generate_test_timestamps(5).split(",")  # Generate 5 timestamps
        try:
            schedule_tasks(timestamps)
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
