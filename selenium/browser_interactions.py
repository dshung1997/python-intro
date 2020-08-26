from selenium import webdriver


class BrowserInteraction:
    def test(self):
        base_url = "https://letskodeit.teachable.com/p/practice"

        driver = webdriver.Chrome()

        # Window Maximize
        driver.maximize_window()
        print("The window is maximized")

        # Open the url
        driver.get(base_url)
        print("The window first loads")

        # Get title
        title = driver.title
        print("Title of this page: ", title)

        # Get the current url
        print("The current url: ", driver.current_url)

        # Browser Refresh
        driver.refresh()
        print("Browser refreshes the 1st time")

        driver.get(base_url)
        print("Browser refreshes the 2nd time")

        # Open another url
        driver.get(
            "https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
        print("The window redirect to another page")

        # Browser back
        driver.back()
        print("The window's going back")

        # Browser forward
        driver.forward()
        print("The window's going forward")

        # Print the page source
        page_source = driver.page_source
        print("The page source :", page_source[0:200])

        # Only one of the following commands is called when there's one open tab
        # driver.close()
        driver.quit()
        print("Quit")


bi = BrowserInteraction()
bi.test()
