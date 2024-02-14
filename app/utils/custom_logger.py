import logging
import os
from logging.handlers import TimedRotatingFileHandler


# Document: https://jonathanserrano.medium.com/deal-with-python-logging-the-easy-way-bf7d41bd48f6
class Logger:
    def __init__(self, name="log", log_level="DEBUG", prefix="local", log_dir="logs"):
        """
        Configures a daily logger
        :param name: logger's name
        :param log_level: logger severity configuration
        :param prefix: a prefix that will be added to the log file
        """

        # 1. Creates a logger using Python's logging facility.
        self.logger = logging.getLogger(name)

        # 2. Sets logger's severity threshold.
        self.logger.setLevel(log_level)

        # 3. Creates a daily log file and stores it at log_dir
        # prepending a prefix.
        fh = TimedRotatingFileHandler(
            os.path.join(log_dir, prefix), 
            when = "midnight", 
            interval = 1
        )

        # 4. Adds the date to the daily log file name.
        fh.suffix = "%Y%m%d.log"

        # 5. Configures the log string format
        # formatter = logging.Formatter('[%(asctime)s][%(levelname)s] {%(pathname)s:%(lineno)d} - %(message)s','%m-%d %H:%M:%S')
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s]%(message)s','%m-%d %H:%M:%S')
        fh.setFormatter(formatter)

        # Adds the handler to the logger
        self.logger.addHandler(fh)

    def get_logger(self):
        return self.logger

logger = Logger().get_logger()