from selenium import webdriver


# class ChromeDriverMac:
#     def test(self):
#         driver = webdriver.Chrome(
#             executable_path="/Users/jayden/Desktop/Code/driver/chromedriver")

#         driver.get("https://www.google.com")


# cc = ChromeDriverMac()
# cc.test()

driver = webdriver.Chrome()

driver.get("https://www.google.com")
