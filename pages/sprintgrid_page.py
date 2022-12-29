import logging
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class SprintGridPage(BaseDriver):
    log = Utils.custom_logger(log_level=logging.WARNING)

    # List of Locators
    ADD_TASK_BUTTON = (By.XPATH, "//button[@aria-label='icon for open/close add form']//mat-icon[@role='img'][normalize-space()='add']")
    SEND_TASK_NAME = (By.ID, "mat-input-6")
    ADD_OPTION_TASK = (By.XPATH, "//button[@type='submit']")
    CLOSE_TASK_BUTTON = (By.XPATH, "//button[@aria-label='icon for open/close add form']")
    IS_TASK_DISPLAYED = (By.XPATH, "(//div[@class='table__task'])[4]")

    ADD_DATE_BUTTON = (By.XPATH, "//button[@aria-label='Icon for open/close add form']")
    CALENDER_ICON = (By.XPATH, "//button[@aria-label='Open calendar']")
    DATE_ON_CALENDER = (By.XPATH, "//div[normalize-space()='30']")
    ADD_OPTION_DATE = (By.XPATH, "//button[@type='submit']")
    CLOSE_DATE_BUTTON = (By.XPATH, "//button[@aria-label='Icon for open/close add form']")

    STATUS_CELL = (By.ID, "mat-expansion-panel-header-4")
    STATUS_FIELD = (By.ID, "mat-input-4")

    REMOVE_TASK_ROW = (By.XPATH, "(//button[@class='mat-focus-indicator table__task-remove mat-icon-button mat-button-base table__task-remove_hidden'])[2]")
    REMOVE_DATE_COLUMN = (By.XPATH, "(//mat-icon[@role='img'][normalize-space()='close'])[2]")

    """create driver instance"""
    def __init__(self, driver, action):
        super().__init__(driver)
        self.driver = driver
        self.action = action

    # For click event
    def do_click(self, locator):
        self.wait_until_element_is_clickable(locator).click()

    # For double click
    def do_double_click(self, locator):
        source_target = self.wait_until_element_is_clickable(locator)
        self.action.double_click(source_target).perform()

    # To move to the element and hover over and click
    def do_move_to_element(self, locator):
        source_target = self.wait_for_presence_of_element(locator)
        self.action.move_to_element(source_target).perform()
        source_target.click()

    # To clear the input field
    def do_clear(self, locator):
        self.wait_until_visibility_of_element_located(locator).clear()

    # To send inputs
    def do_send_keys(self, locator, text):
        self.wait_until_visibility_of_element_located(locator).send_keys(text)

    # To get the text of the web element
    def element_text(self, locator):
        web_element_text = self.wait_until_visibility_of_element_located(locator).text
        self.log.info(web_element_text)

    # For assertion
    def assert_element(self, locator):
        assert_element_ = self.wait_until_visibility_of_element_located(locator)
        return assert_element_.text















