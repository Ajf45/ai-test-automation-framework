from pages.base_page import BasePage

class SearchPage(BasePage):
    def search(self, query):
        self.fill("#search", query)
        self.click("#search-button")

    def get_results(self):
        return self.page.query_selector_all(".result")
    
    