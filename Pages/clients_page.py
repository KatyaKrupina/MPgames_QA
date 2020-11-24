import os
from time import sleep

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Pages.base import BasePage


class ClientsPage(BasePage):
    articles = (By.CSS_SELECTOR, '[class ="card-header text-center"]')
    article = "sub-tree-element"
    blocks = (By.CSS_SELECTOR, '[class="sub-tree"')
    saved_articles = (By.XPATH, "//*[contains(text(), 'Saved articles')]")
    saved_articles_block = (By.CSS_SELECTOR, '[class="right-sub-tree"')

    client_name = (By.CSS_SELECTOR, '[class ="card-title"')
    client_intro = (By.CSS_SELECTOR, '[class ="card-text"')
    client_info = (By.TAG_NAME, 'textarea')
    client_img = (By.ID, 'heroImage')

    slider = (By.CSS_SELECTOR, '[class="ui-slider ui-corner-all ui-slider-horizontal ui-widget ui-widget-content"]')
    download_btn = (By.CSS_SELECTOR, '[class ="btn btn-outline-info"')
    move_to_saved_btn = (By.XPATH, "//*[contains(text(), 'Move to saved')]")
    remove_from_saved_btn = (By.XPATH, "//*[contains(text(), 'Removed from saved')]")

    def __init__(self, driver):
        super().__init__(driver)

    def check_articles_exist(self):
        with allure.step("Checking articles exist"):
            text = self.get_text_in_element(self.articles)
            assert text == 'Articles to read'

    def _get_articles_qty(self, block_index):
        with allure.step("Getting articles quantity"):
            article_block = self.find_elements(self.blocks)
            advertisers = article_block[block_index].find_elements(By.CLASS_NAME, self.article)
            return len(advertisers)

    def get_advertisers_qty(self):
        return self._get_articles_qty(0)

    def get_publishers_qty(self):
        return self._get_articles_qty(1)

    def get_top_level_clients_qty(self):
        return self._get_articles_qty(2)

    def choose_section(self, section_name):
        with allure.step("Choosing article clock by name"):
            section = '//*[contains(text(), ' + "'" + section_name + "'" + ')]'
            self.driver.find_element_by_xpath(section).click()

    def choose_client(self, client_name):
        with allure.step("Choosing client by name"):
            client = '//*[contains(text(), ' + "'" + client_name + "'" + ')]'
            self.wait_for_element((By.XPATH, client)).click()

    def check_client(self, name, info):
        with allure.step("Checking client name and short info"):
            self.wait_for_element(self.client_name)
            client_name = self.get_text_in_element(self.client_name)
            assert client_name == name
            assert self.get_text_in_element(self.client_intro) == info

    def download_info_file(self):
        with allure.step("Downloading info file"):
            self.find_element(self.download_btn).click()
            sleep(1)

    def _get_client_info(self):
        with allure.step("Getting client info"):
            return self.get_text_in_element(self.client_info)

    def compare_text_from_textarea_with_file(self):
        with allure.step("Comparing text from textarea with downloaded file"):
            info = self._get_client_info()
            with open("/tmp/data.txt", "r") as f:
                text_from_file = f.read()
                if text_from_file == info:
                    os.remove("/tmp/data.txt")
                else:
                    os.remove("/tmp/data.txt")
                    raise Exception('Texts are not the same!')

    def check_hero_image_size(self, height, width):
        with allure.step("Checking client image size"):
            img = self.find_element(self.client_img)
            size = img.size
            assert size['height'] == height
            assert size['width'] == width

    def move_slider(self, x, y=0):
        with allure.step("Moving client image slider"):
            move = ActionChains(self.driver)
            slider = self.find_element(self.slider)
            move.click_and_hold(slider).move_by_offset(x, y).release().perform()

    def scroll_textarea(self):
        with allure.step("Scrolling client info to the end"):
            textarea = self.wait_for_element(self.client_info)
            textarea.send_keys(Keys.CONTROL, Keys.END)

    def check_move_to_save_button_is_disabled(self):
        with allure.step("Checking move to save button is disabled"):
            button = self.find_element(self.move_to_saved_btn)
            assert button.is_enabled() is False

    def move_article_to_saved(self):
        with allure.step("Moving article to saved"):
            self.wait_for_element(self.move_to_saved_btn).click()
            articles = self.wait_for_element(self.saved_articles)
            assert articles.is_displayed() is True

    def remove_article_from_saved(self):
        with allure.step("Removing article from saved"):
            self.wait_for_element(self.remove_from_saved_btn).click()

    def get_saved_articles_qty(self, saved_article_block_index):
        with allure.step("Getting saved articles quantity"):
            saved_article_block = self.find_elements(self.saved_articles_block)
            advertisers = saved_article_block[saved_article_block_index].find_elements(By.CLASS_NAME, self.article)
            return len(advertisers)
