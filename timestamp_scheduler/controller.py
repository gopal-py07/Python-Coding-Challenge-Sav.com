from models.scheduler import schedule_tasks
from views.logger import log_message

"""
Controller module that orchestrates scheduling and API calls.
"""


def process_timestamps(timestamps):
    print("List of timestamps (24-hour format, HH:MM:SS): " + ", ".join(timestamps))
    # log_message("List of timestamps (24-hour format, HH:MM:SS): " + ", ".join(timestamps))
    schedule_tasks(timestamps)