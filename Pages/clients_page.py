import os
from time import sleep

from selenium.webdriver.common.by import By

from Pages.base import BasePage


class ClientsPage(BasePage):
    articles = (By.CSS_SELECTOR, '[class ="card-header text-center"]')
    blocks = (By.CSS_SELECTOR, '[class="sub-tree"')
    adv = (By.XPATH, '//*[@id="mainContainer"]/div[2]/div[1]/div/div[2]/div[1]/div')
    btn = (By.XPATH, '//*[@id="mainContainer"]/div[2]/div[1]/div/div[2]/div[1]/button')

    client_name = (By.CSS_SELECTOR, '[class ="card-title"')
    client_info = (By.CSS_SELECTOR, '[class ="card-text"')

    download_btn = (By.CSS_SELECTOR, '[class ="btn btn-outline-info"')
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

    def choose_client(self):
        self.find_element(self.btn).click()
        article_block = self.find_elements(self.blocks)
        advertisers = article_block[0].find_elements(By.CLASS_NAME, "sub-tree-element")
        advertisers[1].click()

    def check_client(self, name, info):
        assert self.get_text_in_element(self.client_name) == name
        assert self.get_text_in_element(self.client_info) == info

    def download_info_file(self):
        self.find_element(self.download_btn).click()
        sleep(1)

    def get_client_info(self):
        return self.get_text_in_element((By.TAG_NAME, 'textarea'))

    def compare_test_from_textarea_with_file(self):
        info = self.get_client_info()
        f = open("/tmp/data.txt", "r")
        text_from_file = f.read()
        assert text_from_file == info
        f.close()
        os.remove("/tmp/data.txt")
