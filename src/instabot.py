from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bot import Bot


class InstaBot(Bot):
    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        sleep(2)
        driver.find_element_by_xpath(
            '/html/body/span/section/main/article/div[2]/div[2]/p/a').click()
        sleep(2)

        username = driver.find_element_by_xpath(
            ('/html/body/span/section/main/div/article'
             '/div/div[1]/div/form/div[2]/div/label/input'))
        username.clear()
        username.send_keys(self.username)

        password = driver.find_element_by_xpath(
            ('/html/body/span/section/main/div/article'
             '/div/div[1]/div/form/div[3]/div/label/input'))
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)


if __name__ == '__main__':
    InstaBot('test', 'test123').login()

