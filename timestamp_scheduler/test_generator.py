"""
Generates sample timestamps for testing.
"""

import random

def generate_test_timestamps(count=5):
    """
    Generates 'count' random timestamps in HH:MM:SS format.
    """
    timestamps = []
    for _ in range(count):
        h = random.randint(0, 23)  # Random hour (0-23)
        m = random.randint(0, 59)  # Random minute (0-59)
        s = random.randint(0, 59)  # Random second (0-59)
        timestamps.append(f"{h:02}:{m:02}:{s:02}")
    
    return ",".join(timestamps)

if __name__ == "__main__":
    print(generate_test_timestamps(7))  # Generate 7 test timestamps
