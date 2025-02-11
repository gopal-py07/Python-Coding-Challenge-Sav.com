"""
Model responsible for scheduling API calls.
"""

import datetime
import threading
import time
from models.api_caller import call_api
from views.logger import log_message

def schedule_tasks(timestamps):
    now = datetime.datetime.now()
    scheduled_tasks = {}

    for ts in timestamps:
        try:
            target_time = datetime.datetime.strptime(ts, "%H:%M:%S").replace(
                year=now.year, month=now.month, day=now.day
            )

            if target_time < now:
                target_time += datetime.timedelta(days=1)

            delay = (target_time - now).total_seconds()

            if delay not in scheduled_tasks:
                scheduled_tasks[delay] = []
            
            scheduled_tasks[delay].append(target_time.strftime("%Y-%m-%d %H:%M:%S"))

        except ValueError:
            log_message(f"Invalid timestamp format: {ts}")

    # Start the execution at the precise delay
    for delay, times in scheduled_tasks.items():
        threading.Thread(target=execute_concurrent_calls, args=(times, delay)).start()

def execute_concurrent_calls(times, delay):
    """Waits for the scheduled time, then runs API calls concurrently."""
    #time.sleep(delay)  # Wait until the scheduled timestamp

    threads = []
    for timestamp in times:
        thread = threading.Thread(target=call_api, args=(timestamp,))
        threads.append(thread)    
        thread.start()  # Start the thread

    for thread in threads:
        thread.join()  # Wait for all threads to finish before moving on
