"""
Model responsible for executing API calls using urllib.request with proper headers.
"""

import urllib.request
from views.logger import log_message
from config import API_URL

def call_api(timestamp):
    try:
        # Add a User-Agent header to avoid 403 Forbidden
        request = urllib.request.Request(
            API_URL,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        )

        with urllib.request.urlopen(request) as response:
            result = response.read().decode("utf-8").strip()
            log_message(f"{timestamp}: Successfully called API at {API_URL}")

    except urllib.error.HTTPError as e:
        pass
    except urllib.error.URLError as e:
        log_message(f"{timestamp}: URL Error - {e.reason}")
    except Exception as e:
        log_message(f"{timestamp}: Exception occurred while calling API - {str(e)}")
