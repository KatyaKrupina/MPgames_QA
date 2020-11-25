from time import sleep

import allure
import pytest

from Pages.profile_page import ProfilePage
from Test_data.profile_data import USER_NAMES, USER_NAMES_SYM


@allure.feature('Profile')
class TestAdvertisers:
    @allure.title('Opening profile from main page')
    def test_open_profile_from_main_page(self, clients_page, browser):
        ProfilePage(browser).show_profile()

    @allure.title('')
    def test_change_only_user_first_name(self, profile_page):
        profile_page.set_user_first_name('Ololo')
        profile_page.click_save_button()
        profile_page.check_last_name_save_error()

    @allure.title('')
    def test_change_only_user_last_name(self, profile_page):
        profile_page.set_user_last_name('Trololo')
        profile_page.click_save_button()
        profile_page.check_first_name_save_error()

    @allure.title('')
    @pytest.mark.parametrize('first_name, last_name', USER_NAMES)
    def test_save_user_name(self, profile_page, first_name, last_name):
        profile_page.set_user_first_name(first_name)
        profile_page.set_user_last_name(last_name)
        profile_page.save_user_info()
        profile_page.driver.refresh()
        assert profile_page.get_saved_name('firstName') == first_name
        assert profile_page.get_saved_name('lastName') == last_name

    @pytest.mark.parametrize('first_name, last_name', USER_NAMES_SYM)
    def test_save_incorrect_user_name(self, profile_page, first_name, last_name):
        profile_page.set_user_first_name(first_name)
        profile_page.set_user_last_name(last_name)
        profile_page.save_user_info()
        profile_page.driver.refresh()
        profile_page.click_save_button()
        profile_page.check_first_name_save_error()
        profile_page.check_first_name_save_error()

    # todo параметризация
    @allure.title('')
    def test_change_card_number(self, profile_page):
        profile_page.switch_to_payment_info()
        sleep(2)
    #
    # # todo параметризация
    # @allure.title('')
    # def test_change_payment_system(self, profile_page):
    #     pass
    #
    # # todo параметризация + дата
    # @allure.title('')
    # def test_save_payment_info(self, profile_page):
    #     pass


