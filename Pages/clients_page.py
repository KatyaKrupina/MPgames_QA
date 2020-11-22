from selenium.webdriver.common.by import By

from Pages.base import BasePage


class ClientsPage(BasePage):
    articles = (By.CSS_SELECTOR, '[class ="card-header text-center"]')
    blocks = (By.CSS_SELECTOR, '[class="sub-tree"')
    adv = (By.XPATH, '//*[@id="mainContainer"]/div[2]/div[1]/div/div[2]/div[1]/div')
    btn = (By.XPATH, '//*[@id="mainContainer"]/div[2]/div[1]/div/div[2]/div[1]/button')
    #
    # login_input = (By.ID, 'loginInput')
    # password_input = (By.ID, 'passwordInput')
    #
    # submit_btn = (By.XPATH, '//*[@id="registrationContainer"]/div/div[3]/button[2]')
    # sign_in_btn = (By.XPATH, '//*[@id="registrationContainer"]/div/div[3]/div/img')

    def __init__(self, driver):
        super().__init__(driver)

    def check_articles_exist(self):
        text = self.get_text_in_element(self.articles)
        assert text == 'Articles to read'

    def _get_articles_qty(self, block_index):
        article_block = self.find_elements(self.blocks)
        advertisers = article_block[block_index].find_elements(By.CLASS_NAME, "sub-tree-element")
        return len(advertisers)

    def get_advertisers_qty(self):
        return self._get_articles_qty(0)

    def get_publishers_qty(self):
        return self._get_articles_qty(1)

    def get_top_level_clients_qty(self):
        return self._get_articles_qty(2)