import allure
import pytest

from Test_data.advertisers_data import ADV_DATA
from Test_data.publishers_data import PUB_DATA
from Test_data.top_clients_data import TOP_CLIENTS_DATA


@allure.feature('Advertisers Info')
class TestAdvertisers:

    @allure.title('Check Advertisers quantity is correct')
    def test_advertisers_qty(self, clients_page):
        advertisers = clients_page.get_advertisers_qty()
        assert advertisers == 2

    @allure.title('Check Advertisers details are correct')
    @pytest.mark.parametrize('name, info', ADV_DATA)
    def test_advertiser_details(self, clients_page, name, info):
        with allure.step('Choosing Advertiser'):
            clients_page.choose_section('Advertisers')
            clients_page.choose_client(name)

        with allure.step('Checking Advertiser details'):
            clients_page.check_client(name, info)
            clients_page.download_info_file()
            clients_page.compare_text_from_textarea_with_file()
            clients_page.check_hero_image_size(300, 300)
            clients_page.move_slider(300)
            clients_page.check_hero_image_size(500, 500)


@allure.feature('Publishers Info')
class TestPublishers:
    @allure.title('Check Publishers quantity is correct')
    def test_publishers_qty(self, clients_page):
        publishers = clients_page.get_publishers_qty()
        assert publishers == 2

    @allure.title('Check Publishers details are correct')
    @pytest.mark.parametrize('name, info', PUB_DATA)
    def test_publisher_details(self, clients_page, name, info):
        with allure.step('Choosing Publisher'):
            clients_page.choose_section('Publishers')
            clients_page.choose_client(name)

        with allure.step('Checking Publisher details'):
            clients_page.check_client(name, info)
            clients_page.download_info_file()
            clients_page.compare_text_from_textarea_with_file()
            clients_page.check_hero_image_size(300, 300)
            clients_page.move_slider(300)
            clients_page.check_hero_image_size(500, 500)


@allure.feature('Top Level Clients Info')
class TestTopLevelClients:

    @allure.title('Check Top level clients quantity is correct')
    def test_top_level_clients_qty(self, clients_page):
        top_level_clients = clients_page.get_top_level_clients_qty()
        assert top_level_clients == 10

    @allure.title('Check Top level clients details are correct')
    @pytest.mark.parametrize('name, info', TOP_CLIENTS_DATA)
    def test_top_level_client_details(self, clients_page, name, info):
        with allure.step('Choosing Top level client'):
            clients_page.choose_section('Top level clients')
            clients_page.choose_client(name)

        with allure.step('Checking Top level client details'):
            clients_page.check_client(name, info)
            clients_page.download_info_file()
            clients_page.compare_text_from_textarea_with_file()
            clients_page.check_hero_image_size(300, 300)
            clients_page.move_slider(300)
            clients_page.check_hero_image_size(500, 500)


@allure.feature('Saved Articles')
class TestSavedArticles:

    @allure.title('Check moving to saved articles is disabled without scrolling')
    def test_move_to_save_button_default(self, clients_page):
        with allure.step('Choosing article without scrolling info'):
            clients_page.choose_section('Advertisers')
            clients_page.choose_client('Test Advertiser')

        with allure.step('Checking save button is disabled'):
            clients_page.check_move_to_save_button_is_disabled()

    @allure.title('Saving articles')
    def test_save_article(self, clients_page):
        with allure.step('Choosing Advertisers and checking, there are two articles to read'):
            clients_page.choose_section('Advertisers')
            assert clients_page.get_advertisers_qty() == 2

        with allure.step('Move article to saved'):
            clients_page.choose_client('Test Advertiser')
            clients_page.scroll_textarea()
            clients_page.move_article_to_saved()

        with allure.step('Checking article is moved to saved and deleted from to read'):
            saved_articles = clients_page.get_saved_articles_qty(0)
            assert saved_articles == 1
            assert clients_page.get_advertisers_qty() == 1

        with allure.step('Move another article to saved'):
            clients_page.choose_client('Adidas')
            clients_page.scroll_textarea()
            clients_page.move_article_to_saved()

        with allure.step('Checking saved articles quantity is increased'):
            saved_articles_new = clients_page.get_saved_articles_qty(0)
            assert saved_articles_new == saved_articles + 1

    @allure.title('Check saved articles have the same functionality as articles to read')
    def test_saved_article_functionality(self, clients_page):
        with allure.step('Move article to saved'):
            clients_page.choose_section('Advertisers')
            clients_page.choose_client('Adidas')
            clients_page.scroll_textarea()
            clients_page.move_article_to_saved()

        with allure.step('Check article'):
            TestAdvertisers().test_advertiser_details(clients_page=clients_page, name='Adidas',
                                                      info='Adidas - is a multinational corporation, founded and '
                                                           'headquartered in Herzogenaurach, Germany, that designs and '
                                                           'manufactures shoes, clothing and accessories')

    @allure.title('Remove article from saved')
    def test_remove_article_from_saved(self, clients_page):
        with allure.step('Move article to saved'):
            clients_page.choose_section('Advertisers')
            assert clients_page.get_advertisers_qty() == 2
            clients_page.choose_client('Test Advertiser')
            clients_page.scroll_textarea()
            clients_page.move_article_to_saved()

        with allure.step('Check article is saved'):
            assert clients_page.get_saved_articles_qty(0) == 1

        with allure.step('Check article is removed from to read articles'):
            assert clients_page.get_advertisers_qty() == 1

        with allure.step('Remove article from saved and check it is returned to to read articles'):
            clients_page.remove_article_from_saved()
            assert clients_page.get_advertisers_qty() == 2

    @allure.title('Check saved articles after refresh')
    def test_save_article_after_refresh(self, clients_page):
        with allure.step('Move article to saved'):
            clients_page.choose_section('Publishers')
            clients_page.choose_client('Youtube')
            clients_page.scroll_textarea()
            clients_page.move_article_to_saved()

        with allure.step('Check article is saved'):
            assert clients_page.get_saved_articles_qty(0) == 1

        with allure.step('Refresh page and check article is still saved'):
            clients_page.driver.refresh()
            assert clients_page.get_saved_articles_qty(0) == 1
