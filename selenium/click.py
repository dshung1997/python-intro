from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Interaction:
    def test(self):
        driver = webdriver.Chrome()

        driver.maximize_window()
        driver.get("https://www.got-it.ai/solutions/excel-chat/")

        # driver.implicitly_wait(10)

        driver.find_element_by_xpath(
            "//button[@id='test-login-button']").click()
        # driver.find_element(By.XPATH, "//button[@id='test-login-button']")

        time.sleep(2)

        driver.find_element_by_xpath(
            "//div[@id='modal-login']//input[@type='email']").send_keys("Hehehe")

        driver.find_element_by_xpath(
            "//div[@id='modal-login']//input[@type='password']").send_keys("Hehehe")

        driver.find_element_by_xpath(
            "//div[@id='modal-login']//button[@type='submit']").click()

        time.sleep(2)


i = Interaction()
i.test()
