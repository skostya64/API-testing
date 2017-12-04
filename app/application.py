from selenium import webdriver


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options=options)

    def quit(self):
        self.driver.quit()