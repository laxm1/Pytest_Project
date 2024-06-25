import time
import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("loginandlogoutsetup")
class BaseClass:

    def verify_element_presence(self,idtype, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((idtype, text)))

    def verify_element_clickable(self,idtype, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((idtype, text)))

    def waitforsometime(self):
        time.sleep(2)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
