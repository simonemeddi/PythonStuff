
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClassWait:

    def __init__(self, driver, type_attr, name_attr, wait_time):
        self.driver = driver
        self.type_attr = type_attr
        self.name_attr = name_attr
        self.wait_time = wait_time

    def WaitConditions(self):
        try:
            element = WebDriverWait(self.driver, self.wait_time).until(
            EC.presence_of_element_located((self.type_attr, self.name_attr))
            )
        finally:
            return element
