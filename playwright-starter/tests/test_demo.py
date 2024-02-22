import pytest

from model.user import User
from pages.sauce_demo_pages.catalog_page import CatalogPage
from pages.sauce_demo_pages.login_page import LoginPage
from  utils.decorators import timeit
from playwright.sync_api import Page
from dynconfig import settings


@pytest.fixture
def login_page(page: Page):
    login_page = LoginPage(page)
    yield login_page


@pytest.fixture
def catalog_page(page: Page):
    catalog_page = CatalogPage(page)
    yield catalog_page

@timeit
def test_valid_user_login(login_page, catalog_page):
    valid_user = User(settings.users.valid_user, settings.passwords.valid_user)
    login_page.goto_login_page()
    login_page.is_loaded()
    login_page.do_login_with(valid_user)
    catalog_page.is_loaded()
    catalog_page.validate_title_is("Products")
    catalog_page.validate_item_nr_text_is(0, "Sauce Labs Backpack")
    catalog_page.iter_items_names()

@timeit
def test_invalid_user_login(login_page):
    user = User(settings.users.invalid_user, settings.passwords.invalid_user)
    login_page.goto_login_page()
    login_page.is_loaded()
    login_page.do_login_with(user)
    login_page.validate_error_message_equals("Epic sadface: Username and password do not match any user in this service")

@timeit
def test_locked_user_login(login_page):
    user = User(settings.users.locked_user, settings.passwords.locked_user)
    login_page.goto_login_page()
    login_page.is_loaded()
    login_page.do_login_with(user)
    login_page.validate_error_message_equals("Epic sadface: Sorry, this user has been locked out.")

@timeit
def test_problem_user(login_page):
    user = User("problem_user", "secret_sauce")
    login_page.goto_login_page()
    login_page.is_loaded()
    login_page.do_login_with(user)

@timeit
def test_performance_user(login_page):
    user = User("performance_glitch_user", "secret_sauce")
    login_page.goto_login_page()
    login_page.is_loaded()
    login_page.do_login_with(user)
