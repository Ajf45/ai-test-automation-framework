from pages.base_page import BasePage

class LoginPage(BasePage):
    def login(self, username, password):
        self.fill("#user-name", username)
        self.fill("#password", password)
        self.click("#login-button")

    def get_error_message(self):
        return self.get_text("h3[data-test='error']")