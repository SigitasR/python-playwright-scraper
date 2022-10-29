from typing import List

from playwright.async_api import Page

from src.page_objects.Pagination import Pagination


class CategoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.pagination = Pagination(self.page)
        self.products_list = page.locator('div.b-products-list--wrapper')

    async def get_page_products_links(self) -> List[str]:
        await self.page.wait_for_load_state('networkidle')
        links: List[str] = []
        await self.pagination.pagination_container.wait_for()
        product_count = await self.products_list.locator('div.b-product--wrap2.b-product--desktop-grid').count()
        print(f'Product boxes in page: {product_count}')
        for i in range(0, product_count):
            product_box = self.products_list.locator(
                'div.b-product--wrap2.b-product--desktop-grid a.b-product-title--desktop').nth(i)
            await product_box.wait_for()
            product_href = await product_box.get_attribute('href')
            if product_href:
                links.append(product_href)
        return links

    async def go_trough_all_pages(self) -> List[str]:
        links: List[str] = []
        while not await self.pagination.is_last_page():
            links.extend(await self.get_page_products_links())
            await self.pagination.click_next()
        links.extend(await self.get_page_products_links())
        return links
