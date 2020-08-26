from selenium import webdriver


class FindByXpathCss:
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()

        driver.get(baseUrl)

        element_by_xpath = driver.find_element_by_xpath("//input[@id='name']")

        if element_by_xpath is not None:
            print("found an element by xpath")

        element_by_css = driver.find_elements_by_css_selector(
            "#displayed-text")

        if element_by_css is not None:
            print("found css element")


ff = FindByXpathCss()
ff.test()
