from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging


class CatalogPage:
    _title = ".title"
    _grid_products = "#inventory_container"
    _item = ".inventory_item"
    _item_name = ".inventory_item_name"

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.logger = logging.getLogger("TestLog")

    def is_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self._title)))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self._grid_products)))
        assert len(self.driver.find_elements(By.CSS_SELECTOR, self._item)) == 6

    def validate_item_nr_text_is(self, index: int, text: str) -> None:
        assert self.driver.find_elements(By.CSS_SELECTOR, self._item_name)[index].text == text

    def validate_title_is(self, text: str) -> None:
        assert self.driver.find_elements(By.CSS_SELECTOR, self._title)[0].text == text

    def iter_items_names(self):
        list_of_items = []
        for i in range(len(self.driver.find_elements(By.CSS_SELECTOR, self._item))):
            list_of_items.append(self.driver.find_elements(By.CSS_SELECTOR, self._item_name)[i].text)
        self.logger.info(list_of_items)
