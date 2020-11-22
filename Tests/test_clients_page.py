import allure


@allure.title('Check Advertisers quantity is correct')
def test_advertisers(clients_page):
    advertisers = clients_page.get_advertisers_qty()
    assert advertisers == 2


@allure.title('Check Publishers quantity is correct')
def test_publishers(clients_page):
    publishers = clients_page.get_advertisers_qty()
    assert publishers == 2


@allure.title('Check Top level clients quantity is correct')
def test_top_level_clients(clients_page):
    publishers = clients_page.get_advertisers_qty()
    assert publishers == 2
