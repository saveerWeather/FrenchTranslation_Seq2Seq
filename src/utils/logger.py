import logging
import os

def setup_logger(log_file="app.log", log_level=logging.INFO):
    """
    Configures the logging settings for the application.

    Args:
        log_file (str): Path to the log file where logs will be saved.
        log_level (int): The logging level (e.g., logging.INFO, logging.DEBUG).
    """
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    logger = logging.getLogger()
    logger.setLevel(log_level)
    
    console_handler = logging.StreamHandler()
    
    file_handler = logging.FileHandler(log_file)

    log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(log_format)
    file_handler.setFormatter(log_format)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

# Example usage:
if __name__ == "__main__":
    logger = setup_logger()
    
    # Log examples:
    logger.info("This is an info message.")
    logger.debug("This is a debug message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
