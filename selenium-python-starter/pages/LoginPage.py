from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from model.user import User


class LoginPage:
    _logo = ".login_logo"
    _username_selector = "#user-name"
    _password_selector = "#password"
    _login_button_selector = "#login-button"
    _error_message_box = "h3[data-test='error']"

    def __init__(self, driver: webdriver):
        self.driver = driver

    def is_loaded(self) -> None:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self._logo)))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self._username_selector)))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self._password_selector)))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self._login_button_selector)))

    def goto_login_page(self) -> None:
        self.driver.get("https://www.saucedemo.com/")

    def do_login_with(self, user: User) -> None:
        self.driver.find_elements(By.CSS_SELECTOR, self._username_selector)[0].click()
        self.driver.find_elements(By.CSS_SELECTOR, self._username_selector)[0].send_keys(user.username)
        self.driver.find_elements(By.CSS_SELECTOR, self._password_selector)[0].click()
        self.driver.find_elements(By.CSS_SELECTOR, self._password_selector)[0].send_keys(user.password)
        self.driver.find_elements(By.CSS_SELECTOR, self._login_button_selector)[0].click()

    def validate_error_message_equals(self, message: str) -> None:
        assert self.driver.find_elements(By.CSS_SELECTOR, self._error_message_box)[0].text == message
