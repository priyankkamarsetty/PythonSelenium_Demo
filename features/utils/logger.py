from loguru import logger
import os
from datetime import datetime

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
logger.add(f"{log_dir}/test_log_{timestamp}.log", level="INFO", rotation="1 MB")
