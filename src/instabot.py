from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from bot import Bot


class InstaBot(Bot):
    url = 'https://www.instagram.com'

    def __try_find_element(self, xpath):
        """Tries to find an element
        Returns the element if found, otherwise closes the browser
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, xpath)))
        except TimeoutException:
            print('Page took too long to load')
            self.quit()

        return element

    def login(self):
        """Login a user"""
        driver = self.driver
        driver.get(self.url)

        login_link = self.__try_find_element(
            '//a[contains(@href, "/accounts/login/")]')
        login_link.click()

        login_btn = self.__try_find_element(
            '//button[@type="submit"]/div[contains(., "Log In")]')
        username = driver.find_element_by_xpath(
            '//input[contains(@name, "username")]')
        username.clear()
        username.send_keys(self.username)
        password = driver.find_element_by_xpath(
            '//input[contains(@name, "password")]')
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

    def get_photos(self, topics):
        """Gets all photos of specific topics
        Returns the urls of the photos
        """
        driver = self.driver
        photo_urls = []

        logged_in = self.__try_find_element(
            '//span[contains(@aria-label, "Profile")]')

        for topic in topics:
            driver.get(f'{self.url}/explore/tags/{topic.lower()}/')
            links = driver.find_elements_by_xpath('//a[contains(@href, "/p/")]')

            for link in links:
                photo_urls.append(link.get_attribute('href'))

        return photo_urls

    def like_photos(self, topics):
        """Likes the photos of specific topics"""
        driver = self.driver
        photo_urls = self.get_photos(topics)

        for url in photo_urls:
            driver.get(url)

            try:
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, 
                        '//span[contains(@aria-label, "Like")]')))
            except TimeoutException:
                print('Page took too long to load')
                continue

            try:
                like_btn = driver.find_element_by_xpath(
                    '//span[contains(@aria-label, "Like") and contains(@class, "24__grey_9")]')
            except NoSuchElementException:
                pass  # photo has already been liked
            else:
                like_btn.click()
                sleep(18)

