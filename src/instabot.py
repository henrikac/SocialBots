from time import sleep
from typing import List

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from bot import Bot
import models


class InstaBot(Bot):
    url = 'https://www.instagram.com'

    def __try_find_element(self, xpath: str):
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

    def login(self) -> None:
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

    def get_photos(self, topics: List[str]) -> List[str]:
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
                url = link.get_attribute('href')

                if not models.get_instaphoto(url):
                    photo_urls.append(url)

        return photo_urls

    def like_photos(self, topics: List[str]) -> None:
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
                continue

            try:
                like_btn = driver.find_element_by_xpath(
                    '//span[contains(@aria-label, "Like") and contains(@class, "24__grey_9")]')
                author = driver.find_element_by_xpath(
                    ('//*[@id="react-root"]/section/main/div/div/'
                    'article/header/div[2]/div[1]/div[1]/h2/a'))
            except NoSuchElementException:
                try:
                    unlike = driver.find_element_by_xpath(
                        '//span[contains(@aria-label, "Unlike")]')
                    author = driver.find_element_by_xpath(
                        ('//*[@id="react-root"]/section/main/div/div/'
                        'article/header/div[2]/div[1]/div[1]/h2/a'))
                except NoSuchElementException:
                    pass
                else:
                    models.add_instaphoto({'url': url, 'author': author.text})
                    sleep(18)
            else:
                like_btn.click()
                models.add_instaphoto({'url': url, 'author': author.text})
                sleep(18)

