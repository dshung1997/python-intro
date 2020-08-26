from selenium import webdriver
from selenium.webdriver.common.by import By


class ImplicitWait:
    def test(self):
        base_url = "https://letskodeit.teachable.com/p/practice"

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get(base_url)

        driver.implicitly_wait(20)

        login_link = driver.find_element(By.XPATH, "//a[@href='/sign_in']")

        login_link.click()


i = ImplicitWait()
i.test()
