import logging
def get_custom_loggers():
    time_format = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt = time_format)

    # Create a logger and set the custom formatter
    logger = logging.getLogger('custom_logger')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Set the log level (optional, can be DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logger.setLevel(logging.DEBUG)
    
    return logger

logger = get_custom_loggers()