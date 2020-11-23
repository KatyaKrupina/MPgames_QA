import os
from time import sleep

import allure


@allure.title('Check Advertisers quantity is correct')
def test_advertisers(clients_page):
    advertisers = clients_page.get_advertisers_qty()
    assert advertisers == 2


@allure.title('Check Publishers quantity is correct')
def test_publishers(clients_page):
    publishers = clients_page.get_publishers_qty()
    assert publishers == 2


@allure.title('Check Top level clients quantity is correct')
def test_top_level_clients(clients_page):
    top_level_clients = clients_page.get_top_level_clients_qty()
    assert top_level_clients == 10


@allure.title('')
def test_top_level_adidas(clients_page):
    clients_page.choose_client()
    clients_page.check_client('Adidas',
                              'Adidas - is a multinational corporation, founded and headquartered in '
                              'Herzogenaurach, Germany, that designs and manufactures shoes, clothing and '
                              'accessories')
    clients_page.download_info_file()
    clients_page.compare_test_from_textarea_with_file()

