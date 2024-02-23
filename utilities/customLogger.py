import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        path = r'C:\Users\apande\PycharmProjects\nopCommerce_V1\logs\automation.log'
        logging.basicConfig(filename=path, format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
