from selenium import webdriver


class FindByIdName:
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()

        driver.get(baseUrl)
        element_by_id = driver.find_element_by_id("name")

        if element_by_id is not None:
            print("found id")

        element_by_name = driver.find_element_by_name("show-hide")

        if element_by_name is not None:
            print("found name")


ff = FindByIdName()
ff.test()
