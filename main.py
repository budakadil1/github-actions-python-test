import logging
import logging.handlers
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    some_variable = os.environ["some_input"]
except KeyError:
    some_variable = "Cannot get input for some reason..."

if __name__ == "__main__":
    logger.info(f"Variable: {some_variable}")
    logger.info("Hello World!!! I work!!!")
