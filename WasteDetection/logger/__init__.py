import os
from datetime import datetime
import logging

# Get the current working directory (where the script is executed)
project_root = os.getcwd()

# Define the log directory and ensure it exists
log_dir = os.path.join(project_root, 'log')
os.makedirs(log_dir, exist_ok=True)

# Generate log file name
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define full log file path
log_file_path = os.path.join(log_dir, log_file)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s"
)

# Test log message
logging.info("Logger initialized. Test log message.")
