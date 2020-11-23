import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver, wait=15):
        self.driver = driver
        self.base_url = "http://localhost:8080/"
        self.wait = WebDriverWait(driver, wait)

    def find_element(self, locator):
        with allure.step("Check if element {} is present".format(locator)):
            try:
                a = self.wait.until(EC.presence_of_element_located(locator))
                return a
            except Exception:
                allure.attach(allure.attach(body=self.driver.get_screenshot_as_png()),
                              name="screenshot_image",
                              attachment_type=allure.attachment_type.PNG)
                raise AssertionError(f"Can't find element by locator {locator}")

    def find_elements(self, locator):
        with allure.step("Check if elements {} are present".format(locator)):
            try:
                a = self.wait.until(EC.presence_of_all_elements_located(locator))
                return a
            except Exception:
                allure.attach(allure.attach(body=self.driver.get_screenshot_as_png()),
                              name="screenshot_image",
                              attachment_type=allure.attachment_type.PNG)
                raise AssertionError(f"Can't find elements by locator {locator}")

    def wait_for_element(self, locator):
        with allure.step("Waiting for element {} to be clickable".format(locator)):
            try:
                a = self.wait.until(EC.element_to_be_clickable(locator))
                return a
            except Exception:
                allure.attach(allure.attach(body=self.driver.get_screenshot_as_png()),
                              name="screenshot_image",
                              attachment_type=allure.attachment_type.PNG)
                raise AssertionError(f"Element {locator} is not clickable")

    def find_text_in_element(self, locator, text):
        with allure.step("Finding text {} in locator {}".format(text, locator)):
            try:
                a = self.wait.until(EC.text_to_be_present_in_element(locator, text))
                return a
            except Exception:
                allure.attach(allure.attach(body=self.driver.get_screenshot_as_png()),
                              name="screenshot_image",
                              attachment_type=allure.attachment_type.PNG)
                raise AssertionError(f"Can't find text in element {locator}")

    def go_to(self):
        with allure.step("Opening url: {}".format(self.base_url)):
            try:
                a = self.driver.get(self.base_url)
                return a
            except Exception:
                allure.attach(allure.attach(body=self.driver.get_screenshot_as_png()),
                              name="screenshot_image",
                              attachment_type=allure.attachment_type.PNG)
                raise AssertionError(f"Can't open url {self.base_url}")

    def get_title(self):
        with allure.step("Getting page title"):
            try:
                a = self.driver.title
                return a
            except Exception:
                allure.attach(allure.attach(body=self.driver.get_screenshot_as_png()),
                              name="screenshot_image",
                              attachment_type=allure.attachment_type.PNG)
                raise AssertionError(f"Can't get title")

    def get_text_in_element(self, locator):
        with allure.step("Getting text"):
            try:
                a = self.wait.until(EC.presence_of_element_located(locator)).text
                return a
            except Exception:
                allure.attach(allure.attach(body=self.driver.get_screenshot_as_png()),
                              name="screenshot_image",
                              attachment_type=allure.attachment_type.PNG)
                raise AssertionError(f"Can't get text in element {locator}")

    def switch_to_current_tab(self):
        with allure.step("Switching to current browser tab"):
            self.driver.switch_to.window(self.driver.window_handles[len(self.driver.window_handles)-1])

    def wait_for_alert(self):
        try:
            a = self.wait.until(EC.alert_is_present())
            return a
        except Exception:
            raise AssertionError("No alert")
