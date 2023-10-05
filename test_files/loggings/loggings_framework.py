import logging
import time

logging.basicConfig(filename=f"test_logs_{time.time()}.log", level=logging.WARNING)


logging.debug("Starting test_case_example...")
logging.info("This is an info message")
logging.warning("this is a warning message")
logging.error("this is an error message")
logging.critical("this is a critical message")
