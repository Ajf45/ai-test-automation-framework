from pages.search_page import SearchPage
from utils.config import BASE_URL   

def test_search_functionality(page):
    search_page = SearchPage(page)
    search_page.navigate(BASE_URL)

    assert "Swag Labs" in page.title()

    

