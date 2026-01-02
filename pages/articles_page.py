from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class ArticlesPage(BasePage):
    """Articles page object"""

    # Locators
    ARTICLE_TITLE = (By.XPATH, "//h2[contains(@class, 'article-title')]")
    ARTICLE_CONTENT = (By.XPATH, "//div[contains(@class, 'article-content')]")
    ARTICLE_AUTHOR = (By.XPATH, "//span[contains(@class, 'author')]")
    RELATED_ARTICLES = (By.XPATH, "//div[contains(@class, 'related-articles')]")

    def is_article_page_loaded(self):
        """Check if article page is loaded"""
        return self.is_element_present(self.ARTICLE_TITLE)

    def is_article_content_displayed(self):
        """Check if article content is displayed"""
        return self.is_element_present(self.ARTICLE_CONTENT)

    def is_author_displayed(self):
        """Check if author is displayed"""
        return self.is_element_present(self.ARTICLE_AUTHOR)

    def is_related_articles_displayed(self):
        """Check if related articles are displayed"""
        return self.is_element_present(self.RELATED_ARTICLES)

    def click_category(self, category_name):
        """Click on category"""
        category_locator = (By.XPATH, f"//a[contains(text(), '{category_name}')]")
        self.click_element(category_locator)

    def get_article_title(self):
        """Get article title"""
        return self.get_text(self.ARTICLE_TITLE) if self.is_element_present(self.ARTICLE_TITLE) else None
