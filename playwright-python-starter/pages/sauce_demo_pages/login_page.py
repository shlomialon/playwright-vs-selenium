from playwright.sync_api import Page, expect
from model.user import User


class LoginPage:

    _logo = ".login_logo"
    _username_selector = "#user-name"
    _password_selector = "#password"
    _login_button_selector = "#login-button"
    _error_message_box = "h3[data-test='error']"

    def __init__(self, page: Page):
        self.page = page

    def is_loaded(self) -> None:
        expect(self.page.locator(self._logo)).to_be_visible()
        expect(self.page.locator(self._username_selector)).to_be_visible()
        expect(self.page.locator(self._password_selector)).to_be_visible()
        expect(self.page.locator(self._login_button_selector)).to_be_visible()

    def goto_login_page(self) -> None:
        self.page.goto("/")

    def do_login_with(self, user: User) -> None:
        self.page.locator(self._username_selector).click()
        self.page.locator(self._username_selector).type(user.username)
        self.page.locator(self._password_selector).click()
        self.page.locator(self._password_selector).type(user.password)
        self.page.locator(self._login_button_selector).click()

    def validate_error_message_equals(self, message: str) -> None:

        expect(self.page.locator(self._error_message_box)).to_have_text(message)
