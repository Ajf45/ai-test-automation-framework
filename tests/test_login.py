from pages.login_page import LoginPage
from utils.data_loader import load_test_data
from utils.config import BASE_URL

data = load_test_data("test_data/login_data.json")

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)

    login_page.login("invalid_user", "wrong_pass")

    error = login_page.get_error_message()
    assert "Epic sadface" in error

