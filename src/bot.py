class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def quit(self):
        self.driver.quit()

