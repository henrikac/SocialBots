from selenium import webdriver


class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def quit(self):
        self.driver.quit()

