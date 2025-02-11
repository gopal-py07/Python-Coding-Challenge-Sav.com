import argparse
from controller import process_timestamps

"""
Main script to accept timestamps from the user and call the controller.
"""


def parse_arguments():
    parser = argparse.ArgumentParser(description="Schedule API calls at specified timestamps.")
    parser.add_argument(
        "timestamps",
        type=str,
        help="Comma-separated list of timestamps in HH:MM:SS format (e.g., 12:30:15,14:00:00)."
    )
    return parser.parse_args()

def main():
    args = parse_arguments()
    timestamps = args.timestamps.split(",")
    process_timestamps(timestamps)

if __name__ == "__main__":
    main()