import os
from time import sleep

import allure
import pytest

from Clients_info.advertisers_data import ADV_DATA
from Clients_info.publishers_data import PUB_DATA
from Clients_info.top_clients_data import TOP_CLIENTS_DATA


class TestAdvertisers:
    @allure.title('Check Advertisers quantity is correct')
    def test_advertisers_qty(self, clients_page):
        advertisers = clients_page.get_advertisers_qty()
        assert advertisers == 2

    @allure.title('Check Advertisers quantity is correct')
    @pytest.mark.parametrize('name, info', ADV_DATA)
    def test_advertiser_details(self, clients_page, name, info):
        clients_page.choose_section('Advertisers')
        clients_page.choose_client(name)
        clients_page.check_client(name, info)
        clients_page.download_info_file()
        clients_page.compare_test_from_textarea_with_file()
        clients_page.check_hero_image_size(300, 300)
        clients_page.move_slider(300)
        clients_page.check_hero_image_size(500, 500)


class TestPublishers:
    @allure.title('Check Publishers quantity is correct')
    def test_publishers_qty(self, clients_page):
        publishers = clients_page.get_publishers_qty()
        assert publishers == 2

    @allure.title('Check Publishers details are correct')
    @pytest.mark.parametrize('name, info', PUB_DATA)
    def test_publisher_details(self, clients_page, name, info):
        clients_page.choose_section('Publishers')
        clients_page.choose_client(name)
        clients_page.check_client(name, info)
        clients_page.download_info_file()
        clients_page.compare_test_from_textarea_with_file()
        clients_page.check_hero_image_size(300, 300)
        clients_page.move_slider(300)
        clients_page.check_hero_image_size(500, 500)


class TestTopLevelClients:
    @allure.title('Check Top level clients quantity is correct')
    def test_top_level_clients_qty(self, clients_page):
        top_level_clients = clients_page.get_top_level_clients_qty()
        assert top_level_clients == 10

    @allure.title('Check Top level clients details are correct')
    @pytest.mark.parametrize('name, info', TOP_CLIENTS_DATA)
    def test_top_level_client_details(self, clients_page, name, info):
        clients_page.choose_section('Top level clients')
        clients_page.choose_client(name)
        clients_page.check_client(name, info)
        clients_page.download_info_file()
        clients_page.compare_test_from_textarea_with_file()
        clients_page.check_hero_image_size(300, 300)
        clients_page.move_slider(300)
        clients_page.check_hero_image_size(500, 500)


