from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
import time


class ExplicitWait:
    def test(self):
        base_url = "https://www.skyscanner.com.vn/transport/flights/han/arn/200830/200906/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&inboundaltsenabled=false&infants=0&outboundaltsenabled=false&preferdirects=false&preferflexible=false&ref=home&rtn=1"

        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(base_url)

        driver.implicitly_wait(10)

        wait = WebDriverWait(driver, 15, poll_frequency=1, ignored_exceptions=[
                             NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])

        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='FqsTabs_fqsTabsWithSparkle__1MQtp']")))

        element.click()

        time.sleep(10)


e = ExplicitWait()
e.test()
