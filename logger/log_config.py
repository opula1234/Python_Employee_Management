# logger.py
import logging

# Configure the logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("api.log"),
        logging.StreamHandler()
    ]
)

# Create logger and export
logger = logging.getLogger("fastapi-app")
