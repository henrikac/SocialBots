from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def try_find_element(self, xpath: str):
        """Tries to find an element
        Returns the element if found, otherwise closes the browser
        """
        try:
            element = WebDriverWait(self.driver, 25).until(
                EC.element_to_be_clickable(
                    (By.XPATH, xpath)))
        except TimeoutException:
            print('Page took too long to load')
            self.quit()

        return element

    def quit(self):
        self.driver.quit()

