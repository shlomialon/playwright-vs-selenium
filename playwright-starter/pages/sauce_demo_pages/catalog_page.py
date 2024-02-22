from playwright.sync_api import Page, expect
import logging


class CatalogPage:

    _title = ".title"
    _grid_products = "#inventory_container"
    _item = ".inventory_item"
    _item_name = ".inventory_item_name"

    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger("TestLog")

    def is_loaded(self):
        expect(self.page.locator(self._title)).to_be_visible()
        expect(self.page.locator(self._grid_products).nth(0)).to_be_visible()
        expect(self.page.locator(self._item)).to_have_count(6)

    def validate_item_nr_text_is(self, index: int, text: str) -> None:

        expect(self.page.locator(self._item_name).nth(index)).to_contain_text(text)

    def validate_title_is(self, text: str) -> None:

        expect(self.page.locator(self._title)).to_have_text(text)

    def iter_items_names(self):

        list_of_items = []

        for i in range(self.page.locator(self._item).count()):

            list_of_items.append(self.page.locator(self._item_name).nth(i).text_content())

        self.logger.info(list_of_items)
