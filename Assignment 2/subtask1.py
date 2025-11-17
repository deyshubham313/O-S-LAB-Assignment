"""
Sub-Task 1: Initialize logging configuration
"""
import logging

logging.basicConfig(
    filename='process_log.txt',
    filemode='w',
    level=logging. INFO,
    format='%(asctime)s - %(processName)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("Logging initialized successfully.")
print(" Logging configuration completed. Check process_log.txt.")
