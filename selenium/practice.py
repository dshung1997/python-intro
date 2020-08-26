from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Practice:

    def __init__(self):
        self.base_url = "https://www.got-it.io/solutions/excel-chat/"

        self.email = "jayden+test02@gotitapp.co"
        self.password = "Asdjsdj2312"

    def __login__(self, driver):
        email_input = driver.find_element_by_xpath(
            "//div[@id='modal-login']//input[@type='email']")
        email_input.send_keys(self.email)

        print("Insert email")

        time.sleep(2)

        password_input = driver.find_element_by_xpath(
            "//div[@id='modal-login']//input[@type='password']")
        password_input.send_keys(self.password)

        print("Insert password")

        time.sleep(2)

        driver.find_element_by_xpath("//button[@id='login-button']").click()

        print("Click the Login button")

    def __purchase__(self, driver):
        # Assert if log-in is successful
        assert(driver.find_element_by_xpath("//a[@id='setting_menu']") != None)

        prev_num_of_sessions = driver.find_element_by_xpath(
            "//button[@id='test-session-balance-header-button']/strong").text
        print("Previous number of session: ", prev_num_of_sessions)

        driver.find_element_by_xpath("//a[@id='setting_menu']").click()
        print("Click the profile button")

        time.sleep(1)

        driver.find_element_by_xpath(
            "//a[@href='/solutions/excel-chat/payment']").click()
        print("Click the payment button")

        time.sleep(2)

        driver.find_element_by_xpath(
            "//button[@id='test-select-plan']").click()
        print("Click the select-plan button")

        time.sleep(3)

        driver.find_element_by_xpath(
            "//div[@id='modal-choose-package']//div[@class='row']/div[3]//button").click()
        print("Click Try For Free on the third option")

        time.sleep(3)

        card = driver.find_element_by_xpath(
            "//div[@id='modal-payment-subscription-engine']//div[@data-braintree-id='upper-container']//div[@data-braintree-id='payment-options-container']/div[1]")
        print("Click Card")

        time.sleep(1)
        card.click()

        submit_button = driver.find_element_by_xpath(
            "//div[@id='modal-payment-subscription-engine']//div[@class='modal-footer']//button")

        if submit_button.text == "PAY NOW":
            submit_button.click()
            print("Click PAY NOW button")
        else:
            # Switch to iframe of card number
            iframe = driver.find_element_by_xpath(
                "//div[@id='modal-payment-subscription-engine']//iframe[@name='braintree-hosted-field-number']")
            driver.switch_to.frame(iframe)
            driver.find_element_by_xpath(
                "//input[@autocomplete='cc-number']").send_keys("4009348888881881")
            print("Insert card number")

            # Switch back to the parent frame
            driver.switch_to.default_content()
            time.sleep(1)

            # Switch to iframe of Expiration Date
            iframe = driver.find_element_by_xpath(
                "//div[@id='modal-payment-subscription-engine']//iframe[@name='braintree-hosted-field-expirationDate']")
            driver.switch_to.frame(iframe)
            driver.find_element_by_xpath(
                "//input[@autocomplete='cc-exp']").send_keys("0423")
            print("Insert expiration date")

            # Switch back to the parent frame
            driver.switch_to.default_content()
            time.sleep(1)

            # Switch to iframe of CVV
            iframe = driver.find_element_by_xpath(
                "//div[@id='modal-payment-subscription-engine']//iframe[@name='braintree-hosted-field-cvv']")
            driver.switch_to.frame(iframe)
            driver.find_element_by_xpath(
                "//input[@autocomplete='cc-csc']").send_keys("234")
            print("Insert CVV")

            # Switch back to the parent frame
            driver.switch_to.default_content()
            time.sleep(1)

            # Switch to iframe of Postal Code
            iframe = driver.find_element_by_xpath(
                "//div[@id='modal-payment-subscription-engine']//iframe[@name='braintree-hosted-field-postalCode']")
            driver.switch_to.frame(iframe)
            driver.find_element_by_xpath(
                "//input[@autocomplete='billing postal-code']").send_keys("75261")
            print("Insert postal code")

            # Switch back to the parent frame
            driver.switch_to.default_content()
            time.sleep(1)

            submit_button = driver.find_element_by_xpath(
                "//div[@id='modal-payment-subscription-engine']//div[@class='modal-footer']//button")

            assert(submit_button.text == "START FREE TRIAL")

            submit_button.click()
            print("Click START FREE TRIAL")

        time.sleep(10)
        new_num_of_sessions = driver.find_element_by_xpath(
            "//button[@id='test-session-balance-header-button']/strong").text
        print("New number of sessions", new_num_of_sessions)
        assert(new_num_of_sessions == "unlimited")

        time.sleep(10)

        print("Done")

    def test(self):
        driver = webdriver.Chrome()

        print("Initializing")

        driver.maximize_window()

        print("Maximize Window")

        driver.get(self.base_url)

        print("Load page")

        driver.implicitly_wait(10)

        driver.find_element_by_xpath(
            "//button[@id='test-login-button']").click()

        print("Click the Login button")

        time.sleep(2)

        self.__login__(driver)

        time.sleep(3)

        self.__purchase__(driver)


p = Practice()
p.test()
