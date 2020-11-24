import os
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Pages.base import BasePage


class ClientsPage(BasePage):
    articles = (By.CSS_SELECTOR, '[class ="card-header text-center"]')
    blocks = (By.CSS_SELECTOR, '[class="sub-tree"')
    adv = (By.XPATH, '//*[@id="mainContainer"]/div[2]/div[1]/div/div[2]/div[1]/div')
    btn = (By.XPATH, '//*[@id="mainContainer"]/div[2]/div[1]/div/div[2]/div[1]/button')

    client_name = (By.CSS_SELECTOR, '[class ="card-title"')
    client_intro = (By.CSS_SELECTOR, '[class ="card-text"')
    client_info = (By.TAG_NAME, 'textarea')

    download_btn = (By.CSS_SELECTOR, '[class ="btn btn-outline-info"')

    slider = (By.CSS_SELECTOR, '[class="ui-slider ui-corner-all ui-slider-horizontal ui-widget ui-widget-content"]')

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

    def choose_section(self, section_name):
        section = '//*[contains(text(), ' + "'" + section_name + "'" + ')]'
        self.driver.find_element_by_xpath(section).click()

    def choose_client(self, client_name):
        client = '//*[contains(text(), ' + "'" + client_name + "'" + ')]'
        self.wait_for_element((By.XPATH, client)).click()

    def check_client(self, name, info):
        self.wait_for_element(self.client_name)
        client_name = self.get_text_in_element(self.client_name)
        assert client_name == name
        assert self.get_text_in_element(self.client_intro) == info

    def download_info_file(self):
        self.find_element(self.download_btn).click()
        sleep(1)

    def _get_client_info(self):
        return self.get_text_in_element(self.client_info)

    def compare_test_from_textarea_with_file(self):
        info = self._get_client_info()
        with open("/tmp/data.txt", "r") as f:
            text_from_file = f.read()
            if text_from_file == info:
                os.remove("/tmp/data.txt")
            else:
                os.remove("/tmp/data.txt")
                raise Exception('Texts are not the same!')

    def check_hero_image_size(self, height, width):
        img = self.find_element((By.ID, 'heroImage'))
        size_before = img.size
        assert size_before['height'] == height
        assert size_before['width'] == width

    def move_slider(self, x, y=0):
        move = ActionChains(self.driver)
        slider = self.find_element(self.slider)
        move.click_and_hold(slider).move_by_offset(x, y).release().perform()

    def scroll_textarea(self):
        textarea = self.wait_for_element(self.client_info)
        textarea.send_keys(Keys.CONTROL, Keys.END)

    def check_move_to_save_button_is_disabled(self):
        button = self.find_element((By.XPATH, "//*[contains(text(), 'Move to saved')]"))
        assert button.is_enabled() is False

    def move_article_to_saved(self):
        self.wait_for_element((By.XPATH, "//*[contains(text(), 'Move to saved')]")).click()
        articles = self.wait_for_element((By.XPATH, "//*[contains(text(), 'Saved articles')]"))
        assert articles.is_displayed() is True

    def remove_article_from_saved(self):
        self.wait_for_element((By.XPATH, "//*[contains(text(), 'Removed from saved')]")).click()

    def get_saved_articles_qty(self, saved_article_block_index):
        saved_article_block = self.find_elements((By.CSS_SELECTOR, '[class="right-sub-tree"'))
        advertisers = saved_article_block[saved_article_block_index].find_elements(By.CLASS_NAME, "sub-tree-element")
        return len(advertisers)
