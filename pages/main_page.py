from .base_page import BasePage
class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.find_element(By.CSS_SELECTOR, "#loginn_link")
        login_link.click()

