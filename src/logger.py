import logging
import os
from datetime import datetime

# Create logs directory
logs_path = "logs"
os.makedirs(logs_path, exist_ok=True)

# Create log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

print("📄 Logger initialized:", LOG_FILE_PATH)  # Debug: Make sure this prints

# Configure logging — critical: force=True
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    force=True
)

logger = logging.getLogger("project_logger")






